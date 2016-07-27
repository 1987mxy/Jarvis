# encoding: utf-8
'''
Created on 2016年1月9日

@author: xiaoyong.mo
'''

class test(object):
	a = None
	def __init__(self):
		pass
	
	def setA(self, av):
		test.a = av
		
	def showA(self):
		print test.a
		
if __name__ == '__main__':
	t1 = test()
	t2 = test()
	t2.setA(3)
	t1.setA(2)
	t2.showA()