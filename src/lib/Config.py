# coding=utf-8
'''
Created on 2015�?5�?22�?

@author: xiaoyong.mo
'''

PROCESS_SWITCH = True

# 日志配置
LOG_SCREEN_LEVEL = 'info'
LOG_PATH = '../log'

# 灯控制USB设备
LIGHT_DEV = '/dev/ttyUSB1'

# 大脑指令访问列表
# CMD_LIST = ['showCtrl', 'neck', 'foot', 'eye', 'light']
CMD_LIST = ['showCtrl', 'neck', 'foot', 'eye']

# 代理转发列表
PROXY_DEFAULT_HOST = 'http://172.16.0.252'
PROXY_CMD_LIST = ['light']

# WOL
MAC_ADDR_MAP = {
			'PC': '4C-CC-6A-30-AA-1E'
			}
BROADCASTADDR = '172.16.0.255'
