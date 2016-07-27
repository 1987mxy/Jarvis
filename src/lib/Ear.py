# encoding: utf-8
'''
Created on 2016年1月9日

@author: xiaoyong.mo
'''
from BaseHTTPServer import HTTPServer
from SocketServer import ThreadingMixIn

import Brain, log

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
			log.info('Jarvis started...')
			server.serve_forever()
		except KeyboardInterrupt:
			log.info('Jarvis exit!')
			server.socket.close()
			Brain.Brain.exit()