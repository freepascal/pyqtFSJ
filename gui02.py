'''QComboBox & QStackedWidget'''
import sys
from PyQt4.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.setGeometry(300, 300, 600, 350)
		self.setWindowTitle('QComboBox & QStackedWidget')
		self.show()
		
		vbox = QVBoxLayout()
		hbox = QHBoxLayout()		
		vbox.addLayout(hbox)
		self.setLayout(vbox)
		
		cbb = QComboBox()
		cbb.insertItem(0, 'option 1')
		cbb.insertItem(1, 'option 2')
		
		self.stacked = QStackedWidget()
		vbox.addWidget(self.stacked)
		
		innerlayout = QHBoxLayout()
		innerlayout.addWidget(cbb)
		innerlayout.addStretch(1)
		hbox.addLayout(innerlayout)	
		
		stack1 = QWidget()
		stack2 = QWidget()
		
		self.stacked.addWidget(stack1)
		self.stacked.addWidget(stack2)
		
		#define stack 1
		layout1 = QHBoxLayout()
		stack1.setLayout(layout1)
		layout1.addStretch(1)
		layout1.addWidget(QLabel('Option 1'))
		
		#define stack 2
		layout2 = QHBoxLayout()
		stack2.setLayout(layout2)
		layout2.addStretch(1)
		layout2.addWidget(QLabel('Option 2'))
		
		#add listeners
		cbb.currentIndexChanged.connect(self.switchOptions)
		
	def switchOptions(self, index):
		self.stacked.setCurrentIndex(index)
		
def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
