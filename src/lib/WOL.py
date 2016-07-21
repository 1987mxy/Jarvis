'''
Created on 2016年7月15日

@author: xiaoyong.mo
'''

from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST
from binascii import a2b_hex

class WOL(object):
	'''
	远程唤醒
	'''

	def __init__(self, broadcastAddr):
		'''
		创建udp套接字
		'''
		self.packagePrefix = 'f' * 12
		self.broadcastAddr = broadcastAddr
		self.udp = socket(AF_INET, SOCK_DGRAM)
		self.udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
		
	def wakeup(self, macAddress):
		wolPackage = a2b_hex(self.packagePrefix + macAddress.replace('-', '') * 16)
		self.udp.sendto(wolPackage, (self.broadcastAddr, 6666))
