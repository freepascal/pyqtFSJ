class parent(object):
	"""constructing from message
	def __init__(self, msg):
		self.value = "Greetings"
	"""
	
	def __init__(self, hello, person):
		self.value = "{0}, {1}".format(hello, person)
		
	def get_value(self):
		return self.value
		
class child(parent):
	pass

c = child('hello', None)
print c.get_value()
