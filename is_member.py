def is_member(x,a):
	flag = False
	i = 0
	while i <= len(a):
		if a[i-1] == x:
			flag = True
			i+=1
		else:
			i+=1
	return flag
var = is_member("aa",[1,2,3,"aaa"])
print(var)

#Do without in operator
