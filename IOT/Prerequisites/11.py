dict1={}
no=int(input("Enter how many values you want to enter in dictionary :"))
i=0
while(i<no):
    hn=input("Enter hindi word : ")
    en=input("Enter english meaning : ")
    dict1[hn]=en
    i+=1
formatting='{:7s} {:7s}'
for (hindi,eng) in dict1.items():
    print("The word :{:7s}'s meaning is :{:7s}".format(hindi,eng))
input()

