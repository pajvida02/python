import sys
print("simple math opertion:sum,sub,multi,div")
def userinput():
	a = int(input("entre the number: "))
	b = int(input("entre the number: "))
opt= input("math opertion:")
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def multi(a,b):
	return a*b
def div(a,b):
	return a/b
if opt == '+':
	print(add(a,b))
elif opt == '-':
	print(sub(a,b))
elif opt == '*':
	print(multi(a,b))
elif opt == '/':
	print(div(a,b))
print('bye')
print("u want exit that program or countine")
response = input()
if response =='exit':
	sys.exit()
elif: 
	print("u type" + response +  '.')
#else:
#	print("to contiune operation")
