def is_overlapping(l1,l2):
	flag = False
	for eachl1 in l1:
		for eachl2 in l2:
			if eachl1 == eachl2:
				flag = True
	return flag


value = is_overlapping([1,2,3,4],[1,6,7,8])
print(value)

