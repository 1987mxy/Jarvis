# encoding: utf-8
'''
Created on 2016年1月9日

@author: xiaoyong.mo
'''
from time import sleep
from sys import path
from lib.LightCtrl import LightCtrl
path.append('./lib')


lc = LightCtrl(1,'/dev/ttyUSB1')

lc.allPowerOff()
print 'allClose:'+str(lc.status())

for i in range(1,5):
	lc.singlePowerOn(i)
	print str(i)+'open:'+str(lc.status())

lc.allPowerOff()
print 'allClose:'+str(lc.status())
lc.allPowerOn()
print 'allOpen:'+str(lc.status())