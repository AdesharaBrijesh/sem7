def score_summary(name,m1,m2,m3):
    sc=[m1,m2,m3]
    mini=min(sc)
    maxi=max(sc)
    avg=(m1+m2+m3)/3
    return (name,maxi,mini,avg)
name=input("Enter name :")
m1=float(input("Enter score from 1st judge :"))
m2=float(input("Enter score from 2nd judge :"))
m3=float(input("Enter score from 3rd judge :"))
name,maxi,mini,avg=score_summary(name,m1,m2,m3)
print(name," : Max ",maxi," , Min ",mini," ,Average ",avg)
