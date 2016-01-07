import sys
import threading
import time

def printCountTo(n):
	count = 0
	while count < n:
		print 'Count is %d' % count
		count += 1
		time.sleep(1)	
		
class StoppableThread(threading.Thread):
	"""Thread class with stop method"""
	def __init__(self, *args, **kwargs):
		threading.Thread.__init__(self, *args, **kwargs)
		self._stop = threading.Event()
		
	def stop(self):
		self._stop.set()
		
	def isstopped(self):
		return self._stop.isSet()
	
def wrapperOfPrintCountTo():
	printCountTo(100)
	
def main():
	t = StoppableThread(target = wrapperOfPrintCountTo)
	t.start()
	t.join()	
	time.sleep(10)
	t.stop()
	
if __name__ == '__main__':
	main()

