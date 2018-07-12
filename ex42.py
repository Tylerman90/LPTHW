## Animal is-a object 
class Animal(object):
	pass

## Dog is-a class
class Dog(Animal):

	def __init__(self, name):
		## dog has-a name
		self.name = name