data = ["cisco","firewall","router","vm"]
print(data)
print("select the following one \n 1- index value \n 2- append \n 3- insert \n 4- sorting \n 5 - remove value \n 5- check contain are in list or not ")
val = input("select the operation : ")
if val == '1':
	a = data.index(input("index value: "))
	if a == data:
		print(True,a)
	else:
		print("sorry the value doen't exits")
	print(a)
elif val == '2':
	a = data.append(input("entre the value:/n "))
	#print(data)
#elif val == '3':
#		a = data.insert(input())
elif val == '4':
	a = data.remove(input("entre that remove contain \n"))
elif val == '5':
	a = input("entre find value: ") in data
	print(a)
else:
	print("sorry the value not entre")

print(data)
