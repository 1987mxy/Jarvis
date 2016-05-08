# encoding: utf-8
'''
Created on 2016年1月9日

@author: xiaoyong.mo
'''
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn

import Brain

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	''' The threaded HTTP server '''

class Ear(object):
	'''
	耳朵，接收外界信息
	'''

	def __init__(self):
		'''
		创建耳朵
		'''
		
	def listening(self):
		try:
			server = ThreadedHTTPServer(('0.0.0.0', 8080), Brain.Brain)
			print 'HTTP server started...'
			server.serve_forever()
		except KeyboardInterrupt:
			print 'Stopping the server!'
			server.socket.close()