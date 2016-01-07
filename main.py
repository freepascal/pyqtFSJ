import sys
import fsj
import threading
from PyQt4.QtGui import *
from FingerTabs import FingerTabBarWidget
from gui import JoinerTab, SplitterTab	
		
class MainWindow(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.initUI()
		
	def initUI(self):
		#define tabs control
		tabControl = QTabWidget()
		tabControl.setTabBar(FingerTabBarWidget(width = 70, height = 50))
		tabControl.setTabPosition(QTabWidget.West)
		
		layout = QVBoxLayout()
		layout.addWidget(tabControl)
		
		#define tabs
		tabJoiner = JoinerTab()
		tabSplitter = SplitterTab()
		tabMore = QWidget()
		
		#add tabs
		tabControl.addTab(tabJoiner, 'Joiner')
		tabControl.addTab(tabSplitter, 'Splitter')
		tabControl.addTab(tabMore, 'More')
		
		self.setLayout(layout)
		self.setWindowTitle('PyQt File Splitter & Joiner')
		self.setGeometry(300, 300, 600, 200)
		self.show()
	
def main():
	app = QApplication(sys.argv)
	mainwindow = MainWindow()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
