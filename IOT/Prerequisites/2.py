
a=input("enter number ")
b=list(a)
c=len(a)
c=c-1
num=0
while (c>=0):
    num=num+int(b[c])
    c=c-1
print("sum=",num)
