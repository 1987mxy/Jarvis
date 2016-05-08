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
	'''
	脖子，控制摄像头的转动
	'''
	cmdList = ['up', 'down', 'left', 'right', 'xStop', 'yStop']

	def __init__(self):
		'''
		创建一个脖子
		'''
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
# 		self.xRudder.ChangeDutyCycle(0)
		self.xPause = True
	
	def yStop(self):
# 		self.yRudder.ChangeDutyCycle(0)
		self.yPause = True
	
	def _action(self, axis, coord):
		position = 11 if coord > 0 else 0.5
		runTime = 0.005
		gapTime = 0.01
		if axis == 'x':
			self.xPause = False
			while not self.xPause:
				self.xRudder.ChangeDutyCycle(position)
				time.sleep(runTime)
				self.xRudder.ChangeDutyCycle(0)
				time.sleep(gapTime)
		else:
			self.yPause = False
			while not self.yPause:
				self.yRudder.ChangeDutyCycle(position)
				time.sleep(runTime)
				self.yRudder.ChangeDutyCycle(0)
				time.sleep(gapTime)
		
