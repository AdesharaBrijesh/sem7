def arm(n1,n2):
    #print("In function")
    a=[]
    i=n1
    while(i<=n2):
        sum1=0
        j=i
        while(j>0):
            sum1+=(j%10)**3
            j=j//10
        if(sum1==i):
            a.append(i)
        i+=1
    print("Armstrong numbers in the range from ",n1," to ",n2," is:")
    for k in a:
        print(k)

n1=int(input("Enter the starting of the range :"))
n2=int(input("Enter the ending of the range :"))
arm(n1,n2)
