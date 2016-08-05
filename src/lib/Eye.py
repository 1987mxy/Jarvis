# coding=utf-8
'''
Created on 2016年4月14日

@author: Free Style
'''

from PIL import Image
import threading, collections, time, io, picamera
import log
from _ctypes import resize

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
class Eye(object):
	'''
	眼睛，接收外界影像信息
	'''
	
	instance = None
	
	frameGap = 0.04

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
		super(Eye, self).__init__()
		self.semaphore = threading.BoundedSemaphore()
		self.buffer = RingBuffer(100)
		self.isRecording = False
		self.timestamp = None
		self.camera = None
		self.width = None
		self.realWidth = None
		self.height = None
		self.realHeight = None
		self.prior_image = None

	# Run the video streaming thread within the singleton instace.
	def run(self):
		try:
			if self.camera == None:
				self.camera = picamera.PiCamera()
				self.camera.framerate = 10
				self.camera.quality = 5
			self.camera.resolution = (self.realWidth, self.realHeight)
			log.info("Camera interface started...")
			stream = io.BytesIO()
			for foo in self.camera.capture_continuous(stream, format='jpeg', use_video_port=True, resize=(self.width, self.height)):
				time.sleep(self.frameGap)
				self.semaphore.acquire()
				stream.seek(0)
				self.buffer.append(stream.getvalue())
				stream.truncate()
				stream.seek(0)
				self.semaphore.release()
				if int(time.time() * 1000) - self.timestamp > 60000:
					# Take the camera to sleep if it has not been used for
					# 60 seconds.
					log.info("No Client connected for 60 sec, camera set to sleep.")
					self.semaphore.acquire()
					self.isRecording = False
					self.semaphore.release()
				if not self.isRecording:
					break
		finally:
			self.camera.stop_preview()
			self.camera.close()
			self.camera = None

	# Get the latest image data from the MJPEG stream
	def getStream(self, width = None, height = None):
		self.timestamp = int(time.time() * 1000)
		if not self.isRecording:
			self.semaphore.acquire()
			self.isRecording = True
			self.semaphore.release()
			self.changeSize(width, height)
			threading.Thread(target=self.run).start()
		stream = ''
		while len(stream) == 0 and self.isRecording:
			stream = self.buffer.get()
			time.sleep(self.frameGap)
		return stream
	
	def changeSize(self, width = None, height = None):
		width = int(width) if width != None else 640
		height = int(height) if height != None else 480
		if self.width != width or self.height != height:
			self.width = width
			self.height = height
			self.realWidth = int(width * 1.6) 
			self.realHeight = int(height * 1.6)
	
	def exit(self):
		self.semaphore.acquire()
		self.isRecording = False
		self.semaphore.release()
