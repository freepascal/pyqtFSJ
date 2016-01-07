import sys
from PyQt4.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.initUI()
	def initUI(self):
		self.setWindowTitle('Sample')
		self.setGeometry(300, 300, 500, 250)
		self.show()
		
		self.stacked = QStackedWidget()
		
		vbox = QVBoxLayout()
		hbox = QHBoxLayout()
		
		first = QRadioButton('First')
		second = QRadioButton('Second')		
		hbox.addWidget(first)
		hbox.addWidget(second)
		
		vbox.addLayout(hbox)
		vbox.addWidget(self.stacked)
		self.setLayout(vbox)
		
		self.stacked.addWidget(QLabel('F'))
		self.stacked.addWidget(QLabel('S'))
		
		first.pressed.connect(self.disp1)
		second.pressed.connect(self.disp2)
		
	def disp1(self):
		self.stacked.setCurrentIndex(0)
		
	def disp2(self):
		self.stacked.setCurrentIndex(1)
		
		
		
def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
