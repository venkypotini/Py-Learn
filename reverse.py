def reverse(strg):
	# strg_list = list(strg)
	# strg_list= (strg_list[::-1])
	# new_strg=""
	# for each in strg_list:
	# 	new_strg+=each
	# print(new_strg)
	lstg = len(strg)
	new_strg =""
	for i in range(lstg):
		new_strg+=strg[lstg-1]
		lstg-=1
	print(new_strg)

reverse("Hallo to All")
#with out using strg_list
