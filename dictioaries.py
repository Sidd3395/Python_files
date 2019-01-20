"""
emp={"name":"khan","tech":"python"}
print (emp)

emp={"name":"khan","tech":"python","tech":"java"}
print(emp)

emp["location"]="hyd"

#works
emp={"name":"khan",{123}:"python","tech":"java"}
#throws error
emp={"name":"khan",[123]:"python","tech":"java"}
#delete
del emp["tech"]

del emp
print (emp)# throws errror

#len

print(len(emp))

#keys
print(emp.keys())

#value
print(emp.values())

#items
print(emp.items())
for i in emp.key():
	print(i)

# copy

newdict=emp.copy()
print(newdict)

#clear
emp.clear()

# update

org={"nameforg":"lync","addrrss":"hyd","estd":2016}
print(org)
print("---------------usind update-------------")
emp.update(org)
print(emp)

org={"nameforg":"lync","addrrss":"hyd","estd":2016,"name":"khan"}
emp={"name":"sid","tech":"python","tech":"java"}
emp.update(org)
print(emp)
print(org)

#pop

emp.pop("tech")
print(emp)

#pop item
emp.popitem()


## user gives 10 we must print 1:1,2:4.....10:100

a=int(input("enter the number"))
numsq={}
for i in range(1,a+1):
	for n in range(1,i+1):
	n=n*n
	numsq[i]=n
print(numsq)

# length of words in a string
a=(input("enter a stmt"))
statment={}
words = a.split(" ")
for i in words:
	b=len(i)
	statment[i]=b
print(statment)
"""
#convert lists to dictionries(wrong)
"""
l1=[1,2,3]
l2=["one","two","three"]


c={}
for i in l1:
	for j in l2:
		c[i]=j
print(c)


# correct

d={}
if len (l1)==len(l2):
	for i in range (len(l1)):
		d[l1[i]=l2[i]]
else
print("enter same lenth")
print(d)

#ZIP
z= zip(l1,l2)
d=dict(z)
print (d)

#dictionary comprehention
d={i:i**2 for i in range (10)}
print(d)

d={i:i**2 for i in range (10) if i %2==0}
print(d)
"""
a=(input("enter a stmt"))
w = a.split()	
statment={i:len(i) for i in (w) if len(w)>4}
print (statment)

#####SETS######

nums={1,2,3,4,5,6,7,8}
print(nums)
print(type(nums))

#blank sets
empset=(())

#add elemenst to set
nums.add(340)

#removes
nums.remove(230)
nums.remove(456)# is not in set wil give error
#discard

num.discard(230)
num.discard(436)# does not give error

#mathamatical uses of sets
s1={10,20,30,40}
s2={20,50,60,80}
s3={10}
s4={100}
#union
print(s1.union(s2))
#or
print(s1|s2)

#intersections
print(s1.intersection(s2))
#or
print(s1&s2)
#diffrence(without comman elements it wil diffrence everything execpt 20 and give it to s1)
print(s2.diffrence(s1))
#or
print(s1-s2)
#isdisjoint(gives TRUE if not comman elements in the sets)
print(s1.isdisjoint(s2))
#issuperset(gives  all the elemenst of S2 must be in S1)
print(s1.issuperset(s2))
#or
print(s1>s2)
#issupset(gives  all the elemenst of S1 must be in S2)
print(s1.issupset(s2))
#or
print(s1<s2)








