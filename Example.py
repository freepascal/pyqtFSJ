import sys
from PyQt4.QtGui import *

class Example(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.initUI()
		
	def initUI(self):
		self.setGeometry(300, 300, 500, 300)
		self.setWindowTitle('Khaang Trann')
		self.show()
		
		hbox = QHBoxLayout()
		self.setLayout(hbox)
		
		ageSpinbox = QSpinBox()
		ageSpinbox.setMinimum(1)
		ageSpinbox.setMaximum(999)
		
		hbox.addWidget(QLabel('Age'))
		hbox.addWidget(ageSpinbox)
def main():
	app = QApplication(sys.argv)
	mainwindow = Example()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
