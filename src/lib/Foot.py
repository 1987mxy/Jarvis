# coding=utf-8
'''
Created on 2016年5月19日

@author: Free Style
'''

import RPi.GPIO as GPIO

class Foot(object):
	'''
	脚，轮子
	'''
	instance = None
	
	# Helper class for the singleton instance.
	class FootHelper():
		def __call__(self, *args, **kw):
			# If an instance of singleton does not exist,
			# create one and assign it to singleton.instance
			if Foot.instance is None:
				Foot.instance = Foot()
			return Foot.instance

	getInstance = FootHelper()

	def __init__(self):
		# Initialize an instance of the singleton class.
		if Foot.instance:
			raise RuntimeError, 'Only one instance of Foot is allowed!'
# 		GPIO.setmode(GPIO.BOARD)
		GPIO.setmode(GPIO.BCM)
		
		
		self.lPin1 = 12
		self.lPin2 = 13
		GPIO.setup(self.lPin1, GPIO.OUT)
		GPIO.setup(self.lPin2, GPIO.OUT)
		
		self.rPin1 = 19
		self.rPin2 = 26
		GPIO.setup(self.rPin1, GPIO.OUT)
		GPIO.setup(self.rPin2, GPIO.OUT)
		
		self.stop()
	
	def stop(self):
		GPIO.output(self.lPin1, GPIO.LOW)
		GPIO.output(self.lPin2, GPIO.LOW)
		
		GPIO.output(self.rPin1, GPIO.LOW)
		GPIO.output(self.rPin2, GPIO.LOW)
	
	def front(self):
		GPIO.output(self.lPin1, GPIO.LOW)
		GPIO.output(self.lPin2, GPIO.HIGH)
		
		GPIO.output(self.rPin1, GPIO.LOW)
		GPIO.output(self.rPin2, GPIO.HIGH)
	
	def rear(self):
		GPIO.output(self.lPin1, GPIO.HIGH)
		GPIO.output(self.lPin2, GPIO.LOW)
		
		GPIO.output(self.rPin1, GPIO.HIGH)
		GPIO.output(self.rPin2, GPIO.LOW)
	
	def right(self):
		GPIO.output(self.lPin1, GPIO.LOW)
		GPIO.output(self.lPin2, GPIO.HIGH)
		
		GPIO.output(self.rPin1, GPIO.HIGH)
		GPIO.output(self.rPin2, GPIO.LOW)
	
	def left(self):
		GPIO.output(self.lPin1, GPIO.HIGH)
		GPIO.output(self.lPin2, GPIO.LOW)
		
		GPIO.output(self.rPin1, GPIO.LOW)
		GPIO.output(self.rPin2, GPIO.HIGH)