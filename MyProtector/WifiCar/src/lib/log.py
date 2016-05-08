# coding=utf-8
'''
Created on 2015å¹?5æœ?22æ—?

@author: xiaoyong.mo
'''

import os, time

import config

recordedLog = []

def log(log, level='debug'):
	global recordedLog
	logLevelList = ['debug', 'info', 'warning', 'error']
	if level not in logLevelList:
		error('"%s" Log Level Error!!!' % level)
	log = "[%s][%s]%s\n" % (time.ctime(), level, log)
	logPath = './log'
	if not os.path.exists(logPath):
		os.mkdir(logPath)
	logBoundary = ''
	for logLevel in logLevelList:
		if logLevel not in recordedLog:
			logBoundary = "\n%s\n" % ('=' * 100)
			recordedLog.append(logLevel)
		logFilename = '%s/%s_%s.log' % (logPath,
										time.strftime('%Y%m%d', time.localtime()),
										logLevel)
		if logLevel == config.LOG_SCREEN_LEVEL:
			print log
		if level == logLevel:
			return True
	
def error(message):
	log(message, 'error')
	os._exit(0)
	
def warning(message):
	log(message, 'warning')
	
def info(message):
	log(message, 'info')
