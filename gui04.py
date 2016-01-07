'''QButtonGroup'''
import sys
from PyQt4.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
	def initUI(self):
		self.setGeometry(300, 300, 400, 200)
		self.setWindowTitle('Sample app')
		self.show()
		
def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()	
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
