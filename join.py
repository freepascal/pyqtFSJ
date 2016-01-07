import sys
import fsj
import random

def printUsage():
	syntax = ''	
	for key in majorParams:
		syntax += '[{0}] '.format(key) if majorParams[key].has_key('default') else '{0} '.format(key)
	print 'Syntax:\n\t{0}'.format(syntax)
	
	instance = ''
	print 'Params\tDescription'
	for key in majorParams:
		print '%s' % key
		print '\t%s' % majorParams[key]['description']
		if majorParams[key].has_key('values'):
			print '\tValue list: %s' % majorParams[key]['values']
			instance += '{0}={1} '.format(
				key, 
				majorParams[key]['values'][					
					random.randrange(
						len(
							majorParams[key]['values']
						)
					)				
				]				
			)			
		if majorParams[key].has_key('default'):	
			print '\tDefault: %s' % majorParams[key]['default']
		elif majorParams[key].has_key('eg'):
			instance += '{0}={1} '.format(
				key,
				majorParams[key]['eg']
			)

	print 'For instance:\n\t%s' % instance
		
def errorExit(msg = None):
	if msg:
		print msg
	else:
		printUsage()
	sys.exit(1)
	
def string2bool(string):
	return True if string.lower() == 'true' else False
		
if __name__ == '__main__':
	majorParams = {
		'source': {
			'description'	: 'The file source to join to one',
			'eg'			: 'filesrc.001'
		},
		'target': {
			'description'	: 'File output',
			'eg'			: 'filetgt'
		},
		'mode'	: {
			'default'		: 'overwrite',
			'values'		: ['overwrite', 'append'],
			'description'	: 'If mode=append the source will be appended to target'
		},
		'autofind': {
			'default'		: 'true',
			'values'		: ['true', 'false'], 
			'description'	: 'Set it true to find next file automatically'
		}	
	}	
	
	allowedParams = majorParams.keys()
	mustDeclareParams = []
	dontNeedDeclareParams = []
	
	argv = {}	
	for key in majorParams:
		if majorParams[key].has_key('default'):
			dontNeedDeclareParams.append(key)
			argv[key] = majorParams[key]['default']
		else:
			mustDeclareParams.append(key)
				
	for i in range(1, len(sys.argv)):		
		s = sys.argv[i].split('=')		
		if s[0] not in allowedParams:
			errorExit()
		elif not s[1]:
			errorExit()
		else:
			argv[s[0].lower()] = s[1]
	
	if len(argv) <> len(mustDeclareParams) + len(dontNeedDeclareParams):
		errorExit()		
	
	if argv['autofind'].lower() not in majorParams['autofind']['values']:
		errorExit()
		
	if argv['mode'].lower() not in majorParams['mode']['values']:
		errorExit()
		
	print 'argv:', argv
	
	fsj.join(
		fileStart 	= argv['source'],
		fileOutput 	= argv['target'],
		joinMode 	= argv['mode'],
		chunkSize 	= 1024*4,			
		autoFind 	= string2bool(argv['autofind'])	
	)	
	
	print 'Finish!'
