# encoding: utf-8
'''
Created on 2016年1月9日

@author: xiaoyong.mo
'''
from sys import path
path.append('./lib')


import threading
import time
from lib import rudder, log, config

import random

switch = True
now = time.time()
random.seed(now)
xRange = None
def randTestX():
	global xRange, switch
	while switch:
		directList = [-1,1]
		directIndex = int(random.random() * 2)
		direct = directList[directIndex]
		directName = 'left' if direct < 0 else 'right'
		sleepTime = round(random.random() * 3, 2)
		log.info('%s, %.2f'%(directName, sleepTime))
		xRange.play(direct)
		time.sleep(sleepTime)
		xRange.stop()
		time.sleep(5)

yRange = None	
def randTestY():
	global yRange, switch
	while switch:
		directList = [-1,1]
		directIndex = int(random.random() * 2)
		direct = directList[directIndex]
		directName = 'up' if direct < 0 else 'down'
		sleepTime = round(random.random() * 3, 2)
		log.info('%s, %.2f'%(directName, sleepTime))
		yRange.play(direct)
		time.sleep(sleepTime)
		yRange.stop()
		time.sleep(5)

if __name__ == "__main__":
	xRange = rudder.Rudder('x', 21)
	yRange = rudder.Rudder('y', 18)
	
	xThread = threading.Thread(target=xRange.run)
	yThread = threading.Thread(target=yRange.run)
	xThread.start()
	yThread.start()
	
	xTest = threading.Thread(target=randTestX)
	yTest = threading.Thread(target=randTestY)
	
	log.log('test begin sleep 5s')
	time.sleep(5)
	
	xTest.start()
	yTest.start()
	
	try:
		time.sleep(3600)
	except KeyboardInterrupt:
		log.info('Process stop!')
# 		xRange.exit()
# 		yRange.exit()
	finally:
		switch = False;
		xRange.exit()
		yRange.exit()