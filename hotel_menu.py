class Lunch:
	def __init__(self, menu):
		self.menu = menu
	def menu_price(self):
		if self.menu == "menu1":
			print("Your Choice {} cost is 12:00".format(self.menu))
		elif self.menu == "menu2":
			print("Your Choice {} cost is 13:40".format(self.menu))
		else:
			print("Error in the menu")

person = Lunch("menu1")
person.menu_price()
