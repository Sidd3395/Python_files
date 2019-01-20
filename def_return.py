'''
#return value
def avg(a,b):
	res=(a+b)/5
	print(res)
	return "python"
print(avg(10,20))

#return variable
def avg(a,b):
	res=(a+b)/5
	print(res)
	return res
print(avg(10,20))
'''
def ao(a,b):
	add=a+b
	print(add)
	return add
	ao(a,b)
def ao(a,b):
	sub=add-b
	print(sub)
	return sub
ao(a,b)
def ao(a,b):
	mul=sub*b
	print(mul)
	return mul
	ao(a,b)
def ao(a,b):
	div=mul/b
	print(div)
	return div
a=int(input ("enter two numbers"))
b=int(input ("enter two numbers"))
ao(a,b)



