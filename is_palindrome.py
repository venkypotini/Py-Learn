def is_palindrome(strg):
	strg_len = int(len(strg)/2)
	strg_list = list(strg)
	flag = "True"
	for item in range(strg_len):
		if strg_list[item] == strg_list[(-1+-(item))]:
			pass
		else:
			flag = "False"

	if flag == "True":
		print("It is Palindrome")
	else:
		print("It is not Palindrome")

is_palindrome("radar")

# Change logic
