from math import *
class Mathey:
    """
    This is Maths assignment"""
    def __init__(self, var1, var2):
        self.var1 = int(var1)
        self.var2 = int(var2)
    def add(self):
        return (self.var1 + self.var2)
    def multiply(self):
        """
        This is multiply funtion, takes var1 and var2 as inputs and"""
        return (self.var1 * self.var2)
    def divide(self):
        # try:
        x = self.var1 /self.var2
        return x
        # except(ZeroDivisionError):
        #     raise ("Division not possible")

    def substract(self):
        return (self.var1 - self.var2)

var1 = input("Enter the first number ")
var2 = input("Enter the second number ")

obj = Mathey(var1, var2)
count = 0
try:

    while True:
        try:
            try:
                choice = int(input("Enter 1 for add, 2 for multiply, 3 for divide, 4 for sub, 5 for exit "))
            except:
                count += 1
                if count >= 3:
                    raise Exception("Please enter integer value")
                else:
                    print("Please enter proper value")

            try:
                if choice == 1:
                    print("The addition for {} and {} is {}".format(obj.var1,obj.var2,obj.add()))
                elif choice == 2:
                    print("The multiply for {} and {} is {}".format(obj.var1,obj.var2,obj.multiply()))
                elif choice == 3:
                    print("The addition for {} and {} is {}".format(obj.var1,obj.var2,obj.divide()))
                elif choice == 4:
                    print("The addition for {} and {} is {}".format(obj.var1,obj.var2,obj.substract()))
                elif choice == 5:
                    break
            except:
                print("Due to internal error opertion not possible")
        except Exception as e:
            print(e)
            raise Exception("Please enter value-2")
except Exception as e:
    print(e)
    print("Check the variables entered")
