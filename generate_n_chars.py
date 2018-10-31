def generate_n_chars(i,x):
	new_string=""
	for i in range(i):
		new_string += str(x)
	return new_string
print(generate_n_chars(10,'x'))

