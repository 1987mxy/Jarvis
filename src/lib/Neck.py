# coding=utf-8
'''
Created on 2016年4月14日

@author: Free Style
'''

import RPi.GPIO as GPIO
import time
import signal
import atexit

class Neck(object):
	#===========================================================================
	# 脖子，控制摄像头的转动
	#===========================================================================

	instance = None
	
	# Helper class for the singleton instance.
	class NeckHelper():
		def __call__(self, *args, **kw):
			# If an instance of singleton does not exist,
			# create one and assign it to singleton.instance
			if Neck.instance is None:
				Neck.instance = Neck()
			return Neck.instance

	getInstance = NeckHelper()

	def __init__(self):
		#=======================================================================
		# 创建一个脖子
		#=======================================================================
		# Initialize an instance of the singleton class.
		if Neck.instance:
			raise RuntimeError, 'Only one instance of Neck is allowed!'
		atexit.register(GPIO.cleanup)
		GPIO.setmode(GPIO.BCM)
		
		xPin = 21
		GPIO.setup(xPin, GPIO.OUT, initial=False)
		self.x = 0
		self.xPause = False
		self.xRudder = GPIO.PWM(xPin, 50) #50HZ
		self.xRudder.start(0)
		
		yPin = 18
		GPIO.setup(yPin, GPIO.OUT, initial=False)
		self.y = 0
		self.yPause = False
		self.yRudder = GPIO.PWM(yPin, 50) #50HZ
		self.yRudder.start(0)
		
	def up(self):
		self._action('y', 1)
	
	def down(self):
		self._action('y', -1)
	
	def right(self):
		self._action('x', -1)
		
	def left(self):
		self._action('x', 1)
		
	def xStop(self):
		self.xPause = True
	
	def yStop(self):
		self.yPause = True

	def reset(self):
		self.xRudder.ChangeDutyCycle(5.5)
		self.yRudder.ChangeDutyCycle(3.2)
		time.sleep(1)
		self.xRudder.ChangeDutyCycle(0)
		self.yRudder.ChangeDutyCycle(0)
	
	def _action(self, axis, coord):
		runTime = 0.005
		gapTime = 0.01
		#=======================================================================
		# 为了防止一直没有收到舵机停止的指令，特设循环安全值。
		# 如果ChangeDutyCycle消耗的时间忽略不计，一次循环大约再0.015秒。
		# 循环100位1.5秒，也就是说如果停止指令没有收到，舵机也会在1.5秒后停止。
		#=======================================================================
		saftTimes = 100
		currTimes = 0
		if axis == 'x':
			position = 11 if coord > 0 else 0.5
			self.xPause = False
			while not self.xPause and currTimes < saftTimes:
				self.xRudder.ChangeDutyCycle(position)
				time.sleep(runTime)
				self.xRudder.ChangeDutyCycle(0)
				time.sleep(gapTime)
				currTimes+=1
		else:
			position = 11 if coord > 0 else 0.5
			self.yPause = False
			while not self.yPause and currTimes < saftTimes:
				self.yRudder.ChangeDutyCycle(position)
				time.sleep(runTime)
				self.yRudder.ChangeDutyCycle(0)
				time.sleep(gapTime)
				currTimes+=1
		
