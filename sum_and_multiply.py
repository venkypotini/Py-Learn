import functools
def sum(l1):
	total = functools.reduce(lambda x,y: x+y,l1)
	return total
total = sum([1,2,3,4])

print("The sum total is {}".format(total))


def multiply(l1):
	total = functools.reduce(lambda x,y: x*y,l1)
	return total
total = multiply([1,2,3,4])

print("The multiply total is {}".format(total))


# Try without for loop

# Use lamda for math function
