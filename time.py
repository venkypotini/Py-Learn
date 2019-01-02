class time:
	def __init__(self, hours, mins):
		self.hours = hours
		self.mins = mins

	def addTime(self,t2):
		pass

	def displayTime(self):
		return self.hours, self.mins

	def displayMinute(self):
		return 60*self.hours + self.mins


t1 = time(2,60)
t2 = time(1,20)
t1.addTime(t2)

print(t1.displayTime())
print(t1.displayMinute())
print(t1.displayMinute())
