## Testing Private and Public methods:
class A:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __testpriv(self):
		print("This is Private funtion")
		print(self.age)

	def testpub(self):
		print("Ths is Public funtion")
		self.__testpriv()

class B:
	def __init__(self, name, age):
		self.__name = name
		self.age = age

	def __func1(self):
		print("This is Private funtion")
		print(self.age)

	def func2(self):
		print("Ths is Public funtion")
		print(self.__name)
		self.__func1()


# Teting Class Inheritance

class parent:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def paren_func(self):
		print("This is parent Func")

class childone(parent):

	def child_func(self):
		print("This is child Func")
		print(self.name)
		print(self.age)








