'''
empset=((1,2,3))
print(type(empset))
'''
##Secret message
'''
alpha='abcdefghijklmnopqrstuvwxyz'
add=3
newword=''
word=input("enter a word")
for i in word:
	if i in alpha:
		position=alpha.find(i)
		newposition=position+add
		word=alpha[newposition]
		newword=newword+word
	else:
		newword=newword+i
print(newword)
'''
'''
##Freiendometer
alpha='abcdefghijklmnopqrstuvwxyz'
vowel='aeiou'
friend='friend'
total=0
names=input("enter your and your friends name")
for alphabet in names:
	if alphabet in vowel:
		total1=alpha.find(alphabet)
		total1=total1+5
	elif alphabet in friend:
		total1=alpha.find(alphabet)
		total1=total1+10
	else:
		total1=alpha.find(alphabet)
	total=total+total1
if total>100:
	print("Friendship bond=",total"Your friendship is strong")
else:
	print("friendship bond=",total"You have a good friendship")

	
'''
import os
print(os.name)