"""
mixed=[10,20,"python",400,[10,"hyd",50.4]]
print(mixed)
mixed.append(1000)# only one element no sub lists can be added
mixed.inser(4,"java")# only one element
mixed.pop()# only one element
mixed.removed(400)
print(mixed.index("python"))
print(mixed.index("python"))
mixed.sort#not possible because all are not numbers


list1=[10,20,30,40,50]
list2=[100,200,300,400]
list1.extend(list2)


for element in mixed:
	print(element)


l1=[1,2,3,4,2,3,1,3,345,7,94,212,3,5,7,8,3]
uni=[]
for i in l1:
	if i not in uni:	
		uni.append(i)
	else:
		rep.append(i)

print(uni)
print(rep)
"""
###for changing it to two lists with numbers and strings sperately.
li=[100,300,"python",400,"english"]
nums=[]
strs=[]
for i in li:
	if type(i) is int:
		nums.append(i)
	else:
		strs.append(i)

print (nums)
print(strs)

### for changing all the lists and sublists elements into a single lists.
li=[100,[230,400,"python"],["hyd",39],200]
for i in li:
	if type(i) is not list:
		nums.append(i)
	else:
		for j in i:
			nums.append(i)
#Create a list and add the elements
a=int(input("enter a list size"))
b=[]
for i range(1,a+1):
	c=int(input("enter your element"))
	b.append(c)
print(b)

#User passes endpoint 10 list must come till 10
a=int(input("enter the list size"))
b=[]
for(i in range(1,a+1)):
	b.append(i)
print(b)

