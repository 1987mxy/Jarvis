# coding=utf-8
'''
Created on 2015�?5�?22�?

@author: xiaoyong.mo
'''

import os, time

import Config

logBoundary = "\n%s\n" % ('=' * 100)
logLevelList = ['debug', 'info', 'warning', 'error']
logHandleList = {}

def error(message):
	_log(message, 'error')
	os._exit(0)
	
def warning(message):
	_log(message, 'warning')
	
def info(message):
	_log(message, 'info')

def debug(message):
	_log(message)

def _log(log, level='debug'):
	global logBoundary, logLevelList, logHandleList
	if level not in logLevelList:
		error('"%s" Log Level Error!!!' % level)
	log = "[%s][%s]%s\n" % (time.ctime(), level, log)
	if not os.path.exists(Config.LOG_PATH):
		os.mkdir(Config.LOG_PATH)
	for logLevel in logLevelList:
		logFilename = '%s/%s_%s.log' % (Config.LOG_PATH,
										time.strftime('%Y%m%d', time.localtime()),
										logLevel)
		if logLevel not in logHandleList.keys():
			logHandleList[logLevel] = open(logFilename, 'a+')
		if logLevel == Config.LOG_SCREEN_LEVEL:
			print log
		logHandleList[logLevel].write(log);
		if level == logLevel:
			return True
