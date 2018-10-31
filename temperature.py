class Temp:

	def convertFahrenheit(self, tmp):
		return (tmp -32)*(5/9)

	def convertCelcius(self, tmp):
		return tmp*(9/5)+32


t1 = Temp()

print(t1.convertCelcius(0))
print(t1.convertFahrenheit(62))
