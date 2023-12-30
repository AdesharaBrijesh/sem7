l1=list(input("enter string values "))
l2=[]
for data in l1:
    l2.append(data)
l1.reverse()
if(l1==l2):
    print("list is palindrome")
else:
    print("Not palindrome")

