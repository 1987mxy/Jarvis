# coding=utf-8
'''
Created on 2016年4月14日

@author: Free Style
'''

import time, os
from BaseHTTPServer import BaseHTTPRequestHandler

import Eye, Neck, LightCtrl, Foot, Config


class Brain(BaseHTTPRequestHandler):
	'''
	大脑，控制一切
	'''
	ctrlCache = {}
	cmdList = Config.CMD_LIST
	myNeck = None
	myFoot = None
	myLightCtrl = None
	
	def do_GET(self):
		print self.path
		pathList = self.path.split('/')
		filename = './resource' + self.path
		if os.path.isfile(filename):
			respContent = self._readFile(filename)
			respHeaders = {}
			ext = os.path.splitext(filename)[-1]
			if ext == '.css':
				respHeaders['content-type'] = 'text/css'
			elif ext == '.js':
				respHeaders['content-type'] = 'application/javascript'
			self._httpSuccess(respContent, respHeaders)
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
			self._httpNotFound()
		
	def showCtrl(self):
		userAgent = self.headers.get('User-Agent').lower()
		if userAgent != None and ('ipad' in userAgent or 'iphone' in userAgent or 'android' in userAgent):
			indexHtml = self._readFile('./resource/index.mobile.html')
		else:
			indexHtml = self._readFile('./resource/index.html')
		self._httpSuccess(indexHtml)
	
	def light(self, action):
		if self.myLightCtrl == None:
			self.myLightCtrl = LightCtrl.LightCtrl(1, Config.LIGHT_DEV)
		if len(action) > 0:
			if action[0] == 'status':
				lightStatus = self.myLightCtrl.status()
				self._httpSuccess(lightStatus[6])
			elif action[0] == 'singlePowerOn' and len(action) >= 2:
				linkNum = int(action[1])
				self.myLightCtrl.singlePowerOn(linkNum)
				self._httpSuccess()
			elif action[0] == 'singlePowerOff' and len(action) >= 2:
				linkNum = int(action[1])
				self.myLightCtrl.singlePowerOff(linkNum)
				self._httpSuccess()
	
	def neck(self, action):
		if self.myNeck == None:
			self.myNeck = Neck.Neck()
		if len(action) > 0:
			cmd = 'self.myNeck.' + action[0]
			eval(cmd)()
			self._httpSuccess()
	
	def foot(self, action):
		if self.myFoot == None:
			self.myFoot = Foot.Foot()
		if len(action) > 0:
			cmd = 'self.myFoot.' + action[0]
			eval(cmd)()
			self._httpSuccess()
	
	def eye(self):
		Eye.Eye.getInstance()
		self.send_response(200)
		self.send_header('Pragma', 'no-cache')
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
				time.sleep(0.04)
		except IOError as e:
			if hasattr(e, 'errno') and e.errno == 32:
				print 'Error: broken pipe'
				self.rfile.close()
				return
			else:
				raise e
	
	def _httpSuccess(self, content = None, headers = None):
		self.send_response(200)
		if content != None:
			if headers == None:
				self.send_header('content-type', 'text/html')
			else:
				for headerKey in headers.keys():
					self.send_header(headerKey, headers[headerKey])
			self.end_headers()
			self.wfile.write(content)
		
	def _httpFail(self):
		self.send_response(500)
		
	def _httpNotFound(self):
		self.send_response(404)
	
	def _readFile(self, filename):
		if filename not in self.ctrlCache.keys():
			_tmpFile = open(filename)
			self.ctrlCache[filename] = _tmpFile.read()
			_tmpFile.close()
		return self.ctrlCache[filename]