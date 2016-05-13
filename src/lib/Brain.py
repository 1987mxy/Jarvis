# coding=utf-8
'''
Created on 2016年4月14日

@author: Free Style
'''

import time, os
from BaseHTTPServer import BaseHTTPRequestHandler

import Eye, Neck, LightCtrl


class Brain(BaseHTTPRequestHandler):
	'''
	大脑，控制一切
	'''
	ctrlCache = {}
	cmdList = ['showCtrl', 'neck', 'eye']
	myNeck = Neck.Neck()
	myLightCtrl = LightCtrl.LightCtrl()
	
	def do_GET(self):
		pathList = self.path.split('/')
		filename = './resource' + self.path
		if os.path.isfile(filename):
			ext = os.path.splitext(filename)[-1]
			if ext == '.css':
				self.send_header('Content-type','text/css')
			self.wfile.write(self._readFile(filename))
		elif len(pathList) < 2 or not pathList[1]:
			self.showCtrl()
		elif pathList[1] in self.cmdList:
			cmd = 'self.' + pathList[1]
			if len(pathList) > 2:
				params = pathList[2:]
				eval(cmd)(params)
			else:
				eval(cmd)()
		else:
			self.send_response(404)
		
	def showCtrl(self):
		userAgent = self.headers.get('User-Agent').lower()
		if userAgent != None and ('ipad' in userAgent or 'iphone' in userAgent or 'android' in userAgent):
			indexHtml = self._readFile('./resource/index.html')
		else:
			indexHtml = self._readFile('./resource/index.mobile.html')
		self.wfile.write(indexHtml)
	
	def light(self, action):
		if len(action) > 0:
			if action[0] == 'status':
				self.myLightCtrl.status()
			elif action[0] == 'singlePowerOn' and len(action) >= 2:
				self.myLightCtrl.singlePowerOn(action[1])
			elif action[0] == 'singlePowerOff' and len(action) >= 2:
				self.myLightCtrl.singlePowerOff(action[1])
	
	def neck(self, action):
		if len(action) > 0:
			cmd = 'self.myNeck.' + action[0]
			eval(cmd)()
			self.send_response(200)
	
	def eye(self):
		Eye.Eye.getInstance()
		self.send_response(200)
		self.send_header('Pragma', 'no-cache');
		self.send_header('Cache-Control', 'no-cache')
		self.send_header('Content-Encoding', 'identify')
		self.send_header('Content-Type', 'multipart/x-mixed-replace;boundary=jpgboundary')
		self.end_headers()
		try:
			while True:
				stream = Eye.Eye.getInstance().getStream()
				self.send_header('Content-type','image/jpeg')
				self.send_header('Content-length', str(len(stream)))
				self.end_headers()
				self.wfile.write(stream)
				self.wfile.write('--jpgboundary\r\n')
				self.send_response(200)
				time.sleep(0.02)
		except IOError as e:
			if hasattr(e, 'errno') and e.errno == 32:
				print 'Error: broken pipe'
				self.rfile.close()
				return
			else:
				raise e
	
	def _readFile(self, filename):
		if filename not in self.ctrlCache.keys():
			_tmpFile = open(filename)
			self.ctrlCache[filename] = _tmpFile.read()
			_tmpFile.close()
		return self.ctrlCache[filename]