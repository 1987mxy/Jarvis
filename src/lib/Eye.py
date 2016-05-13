# coding=utf-8
'''
Created on 2016年4月14日

@author: Free Style
'''

import time, io, picamera, random
from threading import Thread
from PIL import Image
import sys, threading, collections

""" The RingBuffer class provides an implementation of a ring buffer
	for image data """
class RingBuffer(threading.Thread):

	# Initialize the buffer.
	def __init__(self, size_max):
		self.max = size_max
		self.data = collections.deque(maxlen=size_max)
		
	# Append an element to the ring buffer.
	def append(self, x):
		if len(self.data) == self.max:
			self.data.pop()
		self.data.append(x)

	# Retrieve the newest element in the buffer.
	def get(self):
		return self.data[-1] if len(self.data) > 0 else '';

""" The Eye class is a singleton implementation that wraps the
	interface of the Raspicam """
class Eye(threading.Thread):
	'''
	眼睛，接收外界影像信息
	'''
	
	instance = None

	# Helper class for the singleton instance.
	class EyeHelper():
		def __call__(self, *args, **kw):
			# If an instance of singleton does not exist,
			# create one and assign it to singleton.instance
			if Eye.instance is None:
				Eye.instance = Eye()
			return Eye.instance

	getInstance = EyeHelper()

	# Initialization.
	def __init__(self):
		# Initialize an instance of the singleton class.
		if Eye.instance:
			raise RuntimeError, 'Only one instance of Eye is allowed!'
		
		Eye.instance = self
		super(Eye, self).__init__()
		self.start()
		self.isRecording = True
		self.timestamp = int(round(time.time() * 1000))
		self.semaphore = threading.BoundedSemaphore()
		self.camera = None
		self.prior_image = None
		self.stream = None
		self.buffer = RingBuffer(100)

	# Run the video streaming thread within the singleton instace.
	def run(self):
		try:
			if(self.camera == None):
				self.camera = picamera.PiCamera()
				self.camera.resolution = (640, 480)
				self.camera.framerate = 10
				self.camera.quality = 5
			time.sleep(2)
			print "Camera interface started..."
			stream = io.BytesIO()
			for foo in self.camera.capture_continuous(stream, format='jpeg', use_video_port=True):
				self.semaphore.acquire()
				stream.seek(0)
				self.buffer.append(stream.getvalue())
				stream.truncate()
				stream.seek(0)
				self.semaphore.release()
				if int(round(time.time() * 1000)) - self.timestamp > 20000:
					# Take the camera to sleep if it has not been used for
					# 60 seconds.
					print "No Client connected for 20 sec, camera set to sleep."
					self.semaphore.acquire()
					self.isRecording = False
					self.semaphore.release()
				if not self.isRecording:
					break
		finally:
			self.camera.stop_preview()
			self.camera.close()
			self.camera = None

	# Detect motion in the video stream.
	# FIXME: This has to be implemented more sophisticated.
	def detect_motion(self):
		stream = io.BytesIO()
		self.camera.capture(stream, format='jpeg', use_video_port=True)
		stream.seek(0)
		if self.prior_image is None:
			self.prior_image = Image.open(stream)
			return False
		else:
			current_image = Image.open(stream)
			# Compare the current image with the previous image to detect
			# motion.
			result = random.randint(0, 10) == 0
			self.prior_image = current_image
			return result

	# Get the latest image data from the MJPEG stream
	def getStream(self):
		self.timestamp = int(round(time.time() * 1000))
		if(self.isRecording == False):
			self.semaphore.acquire()
			self.isRecording = True
			self.semaphore.release()
			self.run()
		return self.buffer.get()
