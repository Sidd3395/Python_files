#User passes endpoint 10 list must come till 10
"""
a=int(input("enter the list size"))
b=[]
for i in range(1,a+1):
	b.append(i)
print(b)
"""
"""
#user enters endpoint get the even numbers till the endpoint in list
a=int(input("enter the list size"))
b=[]
for i in range(1,a+1):
	if(i%2==0):
		b.append(i)
print(b)
"""
a=int(input("enter the number"))
for i in range(1, a):
    for j in range(65, 65+i):
        a = chr(j)
        print(a, end=" ")
    print()

