import sys
import fsj
import os.path
import random

def printUsage():
	syntax = ''
	for key in majorParams:
		syntax += '{0} '.format(key)
	
	for key in ratioParams:
		syntax += '{0}/'.format(key)
	print 'Syntax:\n\t%s' % syntax[:-1]
	
	instance = ''
	print 'Params\tDescription'
	for key in majorParams:
		print '%s' % key
		print '\t%s' % majorParams[key]['description']
		instance += '{0}={1} '.format(key, majorParams[key]['eg'])
	for key in ratioParams:
		print '%s' % key
		print '\t%s' % ratioParams[key]['description']
		
	for key in ratioParams:
		if ratioParams[key].has_key('suffix'):
			instance_suffx = '{0}={1}{2}'.format(
				key,
				random.randrange(512, 1024),
				ratioParams[key]['suffix'][
					random.randrange(
						len(
							ratioParams[key]['suffix']
						)
					)
				]
			)
			print 'For instance:\n\t%s%s' % (instance, instance_suffx)
		else:
			instance_suffx = '{0}={1}'.format(
				key,
				random.randrange(1, 10)
			)
			print 'For instance:\n\t%s%s' % (instance, instance_suffx)
	
def errorExit(msg = None):
	if msg:
		print msg
	else:
		printUsage()
	sys.exit(1)
	
if __name__ == '__main__':
	majorParams = {
		'source': {
			'description'	: 'The file source to split to several parts, must be exists',
			'eg'			: 'filesrc'
		},
		'target': {
			'description': 'Directory output',
			'eg'			: '/home/outputDir'
		}
	}

	ratioParams = {
		'partsize': {
			'description'	: 'Size of splitted part (suffix: b, kb, mb, gb). Dont need use b for byte',
			'suffix'		: ['b', 'kb', 'mb', 'gb'],			
		},
		'numparts': {
			'description'	: 'The total parts splitted, must be a positive integer',
		}
	}
	
	argv = {}
	
	if len(sys.argv) <> 4:
		errorExit()
		
	allowedParams = set(majorParams.keys()).union(ratioParams.keys())
	
	for i in range(1, len(sys.argv)):
		s = sys.argv[i].split('=')		
		if s[0] not in allowedParams:
			errorExit()
		elif not s[1]:
			errorExit()
		else:
			argv[s[0].lower()] = s[1]
		
	minorArgv = set(argv.keys()) - set(majorParams.keys())
	if len(minorArgv) <> 1:
		errorExit()

	if os.path.isdir(argv['target']):
		argv['target'] = os.path.join(argv['target'], os.path.basename(argv['source']))	
	else:
		os.path.makedirs(argv['target'])
		
	if not os.path.isfile(argv['source']):
		errorExit('File source not found')		
			
	if list(minorArgv)[0] == 'partsize':
		sizeParser = fsj.SizeParser(argv['partsize'])
		argv['partsize'] = sizeParser.getSizeInBytes()
				
		fsj.splitBySize(
			argv['source'],
			argv['target'],
			argv['partsize'],
			chunkSize = 1024*4
		)	
		print 'Finished!'		
			
	elif list(minorArgv)[0] == 'numparts':
		if not argv['numparts'].isdigit():
			errorExit('Parameter numparts must be a integer')
			
		fsj.splitByParts(
			argv['source'],
			argv['target'],
			int(argv['numparts']),
			chunkSize = 1024*4
		)
		print 'Finished!'	
