i=0
ob=open("pr6tx.txt",'w+')
ob.write("Information of Student : \n")
frm='{:<9s} {:<16s} {:<5s} {:<21s}'+"\n"
ob.write(frm.format("Enr no.","Name","Age","Email id"))
while(i<5):
    enr=input("Enter Enrollment no. : ")
    nm=input("Enter name : ")
    age=input("Enter age : ")
    em=input("Enter email : ")
    ob.write(frm.format(enr,nm,age,em))
    i+=1
ob.close()
ob=open("pr6tx.txt",'r')
for line in ob:
		print(line)
ob.close()

