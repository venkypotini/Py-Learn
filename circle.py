import math
class Circle:
	def __init__(self, radius):
		self.radius = radius

	def getArea(self):
		return (math.pi)**self.radius

	def getCircumference(self):
		return 2*math.pi*self.radius

circ = Circle(7)
print(circ.getArea())
print(circ.getCircumference())





