l1=list(input("enter String= "))
a=int(input("enter starting range of substring "))
b=int(input("enter ending range of substring "))
l2=list(input("Enter replacing substring "))
i=a
j=0
while(i<b):
    l1[i]=l2[j]
    j+=1
    i+=1
j=0
while(j<len(l1)):
    print(l1[j],end="")
    j+=1
