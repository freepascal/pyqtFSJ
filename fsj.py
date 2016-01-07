''' file splitter & joiner '''

from os.path import isfile
from os.path import getsize

from math import ceil
from sys import argv

class ExtGenerator:
	def __init__(self, start):
		self.current = start
	
	def next(self):
		result = self.current
		self.current += 1
		return str(result).zfill(3)
		
class SequenceFileExists:
	'''
	fileStart should end with .00x such as .001
	'''
	def __init__(self, fileStart):
		self.extGen = ExtGenerator(
			int(
				fileStart[fileStart.rindex('.')+1:]
			)
		)
		self.pathWithoutExt = fileStart[:fileStart.rindex('.')]
		self.current = None
		
	''' 
	Return True if next file exists
	'''
	def hasNext(self):
		self.current = self.pathWithoutExt + '.' + self.extGen.next()
		return True if isfile(self.current) else False
	
	''' 
	Use with hasNext() for checking next file exists 		
	'''	
	def next(self):
		return self.current	if self.current <> None else self.pathWithoutExt + '.' + self.extGen.next()
		
class SizeParser:
	def __init__(self, string):
		bound = SizeParser.getBound(string)		
		self.number = float(string[:bound])
		self.unit	= string[bound:].lower()			
		if bound == 0 or self.unit not in ['kb', 'mb', 'gb', 'b', '']:
			raise ValueError('IllegalArgumentException')			
		
	def getSizeInBytes(self):
		if self.unit == 'b' or self.unit == '':
			return self.number
		if self.unit == 'kb':
			self.number *= 1024
		elif self.unit == 'mb':
			self.number *= 1024*1024
		elif self.unit == 'gb':
			self.number *= 1024*1024*1024
		return ceil(self.number)
		
	@staticmethod	
	def getBound(string):
		i = 0
		while i < len(string):
			if string[i].isdigit() or string[i] == '.':
				i += 1
				continue
			else:
				break
		return i		
		
def join(fileStart, fileOutput, joinMode, chunkSize = 1024*4, autoFind = True):	
	fw = open(fileOutput, 'wb' if joinMode <> 'append' or not isfile(fileOutput) else 'ab')
	sf = SequenceFileExists(fileStart)	
	try:
		while sf.hasNext():
			try:
				fr = open(sf.next(), 'rb')
				while True:
					chunk = fr.read(chunkSize)
					if chunk:
						fw.write(chunk)
					else:
						break
				'''
				If we use autoFind flag, system will find next file to append to output file
				'''
				if not autoFind:
					break				
			finally:
				fr.close()
	finally:
		fw.close()		
		
def splitBySize(fileSource, fileOutputStart, partSize, chunkSize):
	sf = SequenceFileExists(fileOutputStart + '.001')
	
	if partSize < chunkSize:
		chunkSize = partSize
	
	fileSize = getsize(fileSource)
	if partSize > fileSize:
		partSize = fileSize	
		
	print 'Total size: \t%d\nPart size: \t%d bytes\nChunk size: \t%d' % (fileSize, partSize, chunkSize)
	
	splitted = 0
	
	fr = open(fileSource, 'rb')
	try:
		while splitted < fileSize:
			fw = open(sf.next(), 'wb')
			try:
				splitted_inner = 0
				while True and splitted_inner < partSize:
					chunk = fr.read(chunkSize)
					if chunk:
						fw.write(chunk)
						splitted += len(chunk)
						splitted_inner += len(chunk)
					else:
						break
			finally:
				fw.close()
	finally:
		fr.close()

def splitByParts(fileSource, fileOutputStart, numParts, chunkSize):
	splitBySize(fileSource, fileOutputStart, ceil(getsize(fileSource)/numParts), chunkSize)	
