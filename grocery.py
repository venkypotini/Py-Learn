class Grocery:

    def __init__(self):
        self.shoplist = {}
    x = 10
    def addToList(self, item, number):
        if item not in self.shoplist.keys():
            self.shoplist[item] = number
        else:
            self.shoplist[item] += number

    def returnlist(self):
        print(self.shoplist)
        print(Grocery.x)
obj = Grocery()
