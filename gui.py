import fsj
from PyQt4.QtGui import *
from PyQt4.QtCore import *
	
class GenericThread(QThread):
	def __init__(self, func, *args, **kwargs):
		QThread.__init__(self)
		self.func = func
		self.args = args
		self.kwargs = kwargs
		
	def __del__(self):
		self.wait() 
		
	def run(self):
		self.func(*self.args, **self.kwargs)
		return
			
class SplitterTab(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		
		#editable FIELDS
		self.fileSourceTxtEdit = QLineEdit()
		self.dirTargetTxtEdit = QLineEdit()		
		self.fileSourceTxtEdit.setFixedWidth(400)
		self.dirTargetTxtEdit.setFixedWidth(400)
		
		self.numparts = QRadioButton('equal-size parts')
		self.partsize = QRadioButton('part size')
		self.comboSplitterMode = QComboBox()
		self.comboSplitterMode.insertItem(0, 'equal-size parts')
		self.comboSplitterMode.insertItem(1, 'every xxx bytes')
						
		self.initUI()
		
	def initUI(self):
		#input buttons
		fileSrcBtn = QPushButton('Select')
		dirTgtBtn = QPushButton('Select')
		
		#create layout
		self.inputLayout = QGridLayout()		
		mainLayout = QVBoxLayout()
		self.inputLayout.setSpacing(10)		
		
		#row 1
		self.inputLayout.addWidget(QLabel('File source'), 0, 0)
		self.inputLayout.addWidget(self.fileSourceTxtEdit, 0, 1)
		self.inputLayout.addWidget(fileSrcBtn, 0, 2)
		
		#row 2
		self.inputLayout.addWidget(QLabel('Dir target'), 1, 0)
		self.inputLayout.addWidget(self.dirTargetTxtEdit, 1, 1)
		self.inputLayout.addWidget(dirTgtBtn, 1, 2)
		
		#row 3
		splitterMode = QHBoxLayout()
		splitterMode.addWidget(self.comboSplitterMode)
		splitterMode.addStretch(1)
		
		self.inputLayout.addWidget(QLabel('Split by'), 2, 0)
		self.inputLayout.addLayout(splitterMode, 2, 1)	
		
		#create stackable widget
		self.stackable = QStackedWidget()
		self.stack1 = QWidget()
		self.stack2 = QWidget()
		self.stackable.addWidget(self.stack1)
		self.stackable.addWidget(self.stack2)
		
		self._stack1()
		self._stack2()
		
		#add inner layout to main layout
		mainLayout.addLayout(self.inputLayout)			
		mainLayout.addWidget(self.stackable)
		
		#listener
		self.comboSplitterMode.currentIndexChanged.connect(self.selectSplitterMode)
		
		#set main layout && display window
		self.setLayout(mainLayout)
		self.show()	
		
	def _stack1(self):
		layout = QHBoxLayout()
		layout.addStretch(1)
		layout.addWidget(QLabel('Groovy/Scala developer :-)'))
		self.stack1.setLayout(layout)
		
	def _stack2(self):
		layout = QHBoxLayout()
		layout.addStretch(1)
		layout.addWidget(QLabel('Delphi/Lazarus developer :-)'))
		self.stack2.setLayout(layout)	
			
	def selectSplitterMode(self, index):
		self.stackable.setCurrentIndex(index)
		
def printCountTo(num):
	for i in range(num):
		print 'hello world' + str(i)
		
class JoinerTab(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		
		#construct the fileDialog
		#fileDialog used to select file source && file target
		self.fileDialog = QFileDialog()
						
		#editable FIELDS
		self.fileSourceTxtEdit = QLineEdit()
		self.fileTargetTxtEdit = QLineEdit()		
		self.fileSourceTxtEdit.setFixedWidth(400)
		self.fileTargetTxtEdit.setFixedWidth(400)		
				
		#initialize UI
		self.initUI()
		self.threadPool = []		
		
	def initUI(self):
		#command buttons
		self.cmdStartBtn = QPushButton('Start')
		self.cmdCancelBtn = QPushButton('Cancel')
		
		#input buttons
		fileSourceBtn = QPushButton('Select')
		fileTargetBtn = QPushButton('Save &as')
				
		#main layout (aka global layout)
		glayout = QVBoxLayout()	
				
		inputLayout = QGridLayout()
		cmdLayout = QHBoxLayout()
		cmdLayout.addStretch(1)		
		cmdLayout.addWidget(self.cmdCancelBtn)
		cmdLayout.addWidget(self.cmdStartBtn)
		cmdLayout.addStretch(1)
		glayout.addLayout(inputLayout)
		glayout.addLayout(cmdLayout)
		
		self.setLayout(glayout)
		inputLayout.setSpacing(10)			
					
		#file source
		inputLayout.addWidget(QLabel('File source'), 0, 0)		
		inputLayout.addWidget(self.fileSourceTxtEdit, 0, 1)		
		inputLayout.addWidget(fileSourceBtn, 0, 2)	
		
		#file target
		inputLayout.addWidget(QLabel('File target'), 1, 0)		
		inputLayout.addWidget(self.fileTargetTxtEdit, 1, 1)		
		inputLayout.addWidget(fileTargetBtn, 1, 2)	
		
		#joining mode
		inputLayout.addWidget(QLabel('Mode'), 2, 0)
		
		jmodeLayout = QHBoxLayout()
		
		modeOverwrite = QRadioButton('Overwrite')
		modeOverwrite.setChecked(True)
		
		modeAppend = QRadioButton('Append')
							
		jmodeLayout.addWidget(modeOverwrite)
		jmodeLayout.addWidget(modeAppend)
		jmodeLayout.addStretch(1)
				
		inputLayout.addLayout(jmodeLayout, 2, 1)
		
		#listener
		fileSourceBtn.clicked.connect(self.selectFileSource)
		fileTargetBtn.clicked.connect(self.saveFileTarget)
		self.cmdStartBtn.clicked.connect(self.startJoining)
		QObject.connect(self.cmdCancelBtn, SIGNAL('released()'), self.cancelJoining)
		
		#display the window
		self.show()
		
	def selectFileSource(self):		
		self.fileSourceTxtEdit.setText(self.fileDialog.getOpenFileName(caption = 'Select file source'))
		
	def saveFileTarget(self):
		self.fileTargetTxtEdit.setText(QFileDialog.getSaveFileName(caption = 'Save file target'))
		
	def startJoining(self):
		#disable button 'Start'
		self.cmdStartBtn.setCheckable(False)
		self.threadPool.append(		
			GenericThread(						
				self.join
			)
		)
		self.threadPool[len(self.threadPool)-1].start()
				
	def join(self):		
		fsj.join(
			unicode(self.fileSourceTxtEdit.displayText()),
			unicode(self.fileTargetTxtEdit.displayText()),
			'overwrite',
			chunkSize = 1024*4,
			autoFind = True
		)
		
	def cancelJoining(self):
		self.workThread.terminate()
		#delete text fields related		
		self.fileSourceTxtEdit.clear()
		self.fileTargetTxtEdit.clear()
		#enable button 'Start'
		self.cmdStartBtn.setCheckable(True)
