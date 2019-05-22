#program about list 
os = []
while True:
	print("entre list os name" + str(len(os)+ 1 ))
	name = input()
	if name == '':
		break
	os = os + [name]
print("end")
print(os)
for name in os:
	 print(name)

