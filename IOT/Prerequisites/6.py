i=0
l=[]
sum=0
while(i<5):
    print("enter marks for subject ",i)
    a=int(input())
    l.append(a)
    sum=sum+a
    i=i+1
avg=sum/5
print("average is= ",avg)
if (avg >= 90):
	print("Excellent Marks")
elif (avg >= 80):
	print("very Good")
elif (avg >= 60):
	print("Average")
elif (avg >= 45):
	print("Not Bad")
elif (avg >= 30):
	print("Try Hard next time")
else:
	print("FAIL")