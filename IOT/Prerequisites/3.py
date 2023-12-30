
no=int(input("enter number= "))
i=2
flag=0
while(i<no):
    if(no%i==0):
        flag=1
        break
    i=i+1
    
if(flag==1):
    print(no,"is not prime")
else:
    print(no,"is prime")
