def max_func(*args):
	max = args[0]
	for each in args:
		if each >= max:
			max = each
	return max

max_value = max_func(1,2,3,4,1,1)
print(max_value)
