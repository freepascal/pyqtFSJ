'''QListWidget & QstackedWidget '''
import sys
from PyQt4.QtGui import *

class MainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.initUI()
		
	def initUI(self):		
		self.setGeometry(300, 300, 600, 350)
		self.setWindowTitle('QStackedWidget')
		self.show()
		
		self.leftList = QListWidget()
		#populating list
		self.leftList.insertItem(0, 'JVM')
		self.leftList.insertItem(1, 'Native')
		self.leftList.insertItem(2, 'Interpreter')
		
		#stacks
		self.stack = QStackedWidget()
		self.stack1 = QWidget()
		self.stack2 = QWidget()
		self.stack3 = QWidget()
		
		self.stack1UI()
		self.stack2UI()
		self.stack3UI()
		
		self.stack.addWidget(self.stack1)
		self.stack.addWidget(self.stack2)
		
		#main layout
		layout = QHBoxLayout()
		layout.addWidget(self.leftList)
		layout.addWidget(self.stack)
		self.setLayout(layout)
		self.leftList.currentRowChanged.connect(self.display)
		
	def stack1UI(self):
		layout = QFormLayout()
		cbb = QComboBox()
		cbb.insertItem(0, 'Java')
		cbb.insertItem(1, 'Groovy')
		cbb.insertItem(2, 'Scala')		
		layout.addRow(QLabel('Lang'), cbb)
		self.stack1.setLayout(layout)
		
	def stack2UI(self):
		layout = QFormLayout()
		sex = QHBoxLayout()
		sex.addWidget(QRadioButton("Male"))
		sex.addWidget(QRadioButton("Female"))
		layout.addRow(QLabel("Sex"),sex)
		layout.addRow("Date of Birth",QLineEdit())		
		self.stack2.setLayout(layout)
		
	def stack3UI(self):
		pass
		
	def display(self, index):
		self.stack.setCurrentIndex(index)

def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
