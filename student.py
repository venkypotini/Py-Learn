class student:
	def __init__(self, name, rollnum):
		self.name = name
		self.rollnum = rollnum

	def display(self):
		return self.name, self.rollnum
	def setAge(self, age):
		self.age = age

	def setMarks(self, mark1, mark2):
		self.sub1 = mark1
		self.sub2 = mark2

venky = student("Venky", 47)

print(venky.display())
venky.setAge(38)
venky.setMarks(60,79)
print(venky.sub1)
print(venky.sub2)


