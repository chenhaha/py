# -*- coding:utf-8 -*-
import threading
import Queue

queue_tmp = Queue.Queue()

class producer(threading.Thread):
	def __init__(self,name):
		super(producer,self).__init__()
		self.name = name
		self.i = 0
		
	def run(self):
		while self.i < 10:
			queue_tmp.put(0)
			print "Producer: %s create a product" % (self.name,)
			print "Producer: %s put a product into queue" % (self.name,)
			self.i += 1
			
class consumer(threading.Thread):
	def __init__(self,name):
		super(consumer,self).__init__()
		self.name = name
		self.i = 0
		
	def run(self):
		while self.i <5:
			queue_tmp.get()
			print "Consumer: %s get a product" % (self.name,)
			self.i += 1
			
if __name__=="__main__":
	for x in xrange(2):
		producer(str(x)).start()
		
	for x in xrange(10,15):
		consumer(str(x)).start()