"""a=input("enter a number")
if a.isdigit():
	a=int(a)
	if(a%3==0 and a%5==0):
		Print("Multiple of 3 and 5")
	elif (a%3==0):
		Print("Multiple of 3")
	elif (a%5==0):
		Print("Multiple of 5")
	else:
		Print("nothing")
else:
	print("enter a valid number")

"""
"""
#print("The Octal representation of 29.5 is " + oct(29)) 
def addition(n): 
    return n + n 
""" 
"""
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 
"""
a=int(input("enter a number"))
for j in range (1,a+1):
	for i in range (1,j+1):
		print(i, end="")
	print()