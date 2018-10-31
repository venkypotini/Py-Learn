class time:
	def __init__(self, hours, mins):
		self.hours = hours
		self.mins = mins

	def addTime():
		pass

	def displayTime(self):
		return self.hours, self.mins

	def displayMinute(self):
		return 60*self.hours + self.mins


t1 = time(2,60)

print(t1.displayTime())
print(t1.displayMinute())



