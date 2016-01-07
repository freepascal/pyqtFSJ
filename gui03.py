'''QButtonGroup & QStackedWidget'''
import sys
from PyQt4.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
		
	def initUI(self):
		self.setGeometry(300, 300, 500, 300)
		self.show()
		
		layout = QVBoxLayout()
		
		btngrp = QButtonGroup()
		
		#layout contains button 1, button 2, button 3
		hbox = QHBoxLayout()
		btn1 = QRadioButton('Button 1')
		btn2 = QRadioButton('Button 2')
		btn3 = QRadioButton('Button 3')
		hbox.addWidget(btn1)
		hbox.addWidget(btn2)
		hbox.addWidget(btn3)
		
		btngrp.addButton(btn1)
		btngrp.addButton(btn2)
		btngrp.addButton(btn3)
		
		layout.addLayout(hbox)
		
		#STACKED WIDGET
		self.stacked = QStackedWidget()
		#define stacks
		stack1 = QWidget()		
		stack2 = QWidget()
		stack3 = QWidget()
				
		layout1 = QHBoxLayout()
		layout1.addStretch(1)
		layout1.addWidget(QLabel('Button 1'))
		stack1.setLayout(layout1)
		
		layout2 = QHBoxLayout()
		layout2.addStretch(1)
		layout2.addWidget(QLabel('Button 2'))
		stack2.setLayout(layout2)
		
		layout3 = QHBoxLayout()
		layout3.addStretch(1)
		layout3.addWidget(QLabel('Button 3'))
		stack3.setLayout(layout3)
		
		self.stacked.addWidget(stack1)
		self.stacked.addWidget(stack2)	
		self.stacked.addWidget(stack3)		
		
		self.setLayout(layout)
		layout.addWidget(self.stacked)
		
		#listener
		btngrp.buttonClicked.connect(self.btnpressed)
		
	def btnpressed(self, i):
		self.stacked.setCurrentIndex(i)
	
def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
