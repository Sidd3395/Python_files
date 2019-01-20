"""
time=input("enter the time ")
if len(time)==10:
	hh=int(time[0:2])
	mm=int(time[3:5])
	ss=int(time[6:8])
	if hh < 12:
		if time[8:11]=="pm":
			hh==hh+12
			print("%d:%d:%d"%(hh,mm,ss))
		else:
			hh=hh
			print("%d:%d:%d"%(hh,mm,ss))
	elif hh==12:
		hh==00
		print("%d:%d:%d"%(hh,mm,ss))
	else:
		print('Enter Hours less than 13')
else:
	print("time is unrecogonised")	 
"""
n=int(input("enter a number"))
count=0
for i in range (1,n+1) :
    if n% i==0:
        print("It is a factor of  " +str(i)+ "is")
        count+=1
if count >2:
    print("It is a composite num")
else:
    print("it is a prime number")
