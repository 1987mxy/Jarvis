#encoding=utf-8
'''
Created on 2014年2月24日

@author: Moxiaoyong
'''

import serial
from struct import pack, unpack

moduleAddress = 1
portNumber = 2

class LightCtrl:
	def __init__(self, module, port):
		self.module = module
		self.port = port - 1
		self.package = None
		self.comm = None
		self.connect()

	def connect(self):
		if self.comm == None:
			self.comm = serial.Serial(portNumber)
	
	def send(self):
		self.comm.write(self.package)
		
	def receive(self):
		package = self.comm.read(serial.EIGHTBITS)
		data = unpack('BBBBBBBB', package)
		return data
	
	def reset(self):
		self.package = None
	
	def close(self):
		self.comm.close()
		self.comm = None;
		
	def genPackage(self, packageType, data):
		packageData = [0x55,
						self.module % 256,
						packageType]
		packageData += data
		packageSum = sum(packageData)
		packageData.append(packageSum % 256)
		self.package = pack('<BBBBBBBB', *packageData)
	
	def allPowerOn(self):
		data = [0] * 4
		data[2:] = [0xff, 0xff]
		self.genPackage(0x13, data)
		self.send()
		self.reset()
	
	def allPowerOff(self):
		data = [0] * 4
		self.genPackage(0x13, data)
		self.send()
		self.reset()
	
	def status(self):
		data = [0] * 4
		self.genPackage(0x10, data)
		self.send()
		self.reset()
		return self.receive()
		
	def singlePowerOn(self, linkNum):
		data = [0] * 4
		data[linkNum - 1] = 2
		self.genPackage(0x01, data)
		print self.package.__repr__()
		self.send()
		self.reset()
	
	def singlePowerOff(self, linkNum):
		data = [0] * 4
		data[linkNum - 1] = 1
		self.genPackage(0x01, data)
		self.send()
		self.reset()
