import sys
print("simple math opertion:sum,sub,multi,div")
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
if opt == 'sum':
	print(add(a,b))
elif opt == 'sub':
	print(sub(a,b))
elif opt == 'multi':
	print(multi(a,b))
elif opt == 'div':
	print(div(a,b))
print('bye')
