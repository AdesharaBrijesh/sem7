import sqlite3
def adddata() :
    e_no = int(input("Enter student Enrollment no: "))
    name = input("Enter student Name: ")
    pwd = input("Enter student Password: ")
    age = int(input("Enter student Age: "))
    email = input("Enter student Email: ")
    add = input("Enter student Address: ")
    try :
        qry = "INSERT INTO STUINFO(EN_NO,NAME,PASSWORD,AGE,EMAIL,ADDRESS)         VALUES (%d,'%s','%s',%d,'%s','%s')"%(e_no,name,pwd,age,email,add) 
        conn.execute(qry)
        conn.commit()
        print("Data inserted Successfully!!")
    except :
        print("Data already exists!!")
        
def deldata(conn) :
    e_no = int(input("Enter student Enrollment no which you want to delete: "))
    try :
        conn.execute("DELETE from STUINFO where EN_NO=%d;"%(e_no))
        conn.commit()
        print("Data deleted Successfully!!")
    except :
        print("Data not exists!!")

def updatedata(conn) :
    e_no = int(input("Enter student Enrollment no: "))
    name = input("Enter student New Name: ")
    pwd = input("Enter student New Password: ")
    age = int(input("Enter student New Age: "))
    email = input("Enter student New Email: ")
    add = input("Enter student New  Address: ")
    try :
        conn.execute("UPDATE STUINFO set NAME = '%s',PASSWORD = '%s',AGE = %d,EMAIL = '%s',ADDRESS = '%s'         where EN_NO = %d"%(name,pwd,age,email,add,e_no))
        conn.commit()
        print("Data updated Successfully!!")
    except :
        print("Data not exists!!")

def searchdata(conn) :
    e_no = int(input("Enter student Enrollment no: "))
    formatting = " {:3} {:10} {:10} {:3} {:30} {:50} "
    try :
        cur = conn.cursor()
        cur.execute("SELECT * from STUINFO where EN_NO = %d"%(e_no))
        i = cur.fetchone()
        print(formatting.format("ENO","NAME","PASSWORD","AGE","EMAIL","ADDRESS"))
        #print("\n")
        print(formatting.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    except :
        print("Data not exists!!")
        
def disdata(conn) :
    formatting = " {:3} {:10} {:10} {:3} {:30} {:50} "
    try :
        cursor = conn.execute("SELECT * from STUINFO")
        print(formatting.format("ENO","NAME","PASSWORD","AGE","EMAIL","ADDRESS"))
        #print("\n")
        for i in cursor :
            print(formatting.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    except :
        print("Data not exists!!")

  
conn = sqlite3.connect("studentinfo.db")
print("Opened database successfully")
try :
    conn.execute('''CREATE TABLE STUINFO
    (EN_NO INT PRIMARY KEY NOT NULL, 
    NAME TEXT NOT NULL,
    PASSWORD CHAR(10) NOT NULL,
    AGE INT NOT NULL, 
    EMAIL CHAR(30), 
    ADDRESS CHAR(50))''')
    print("Table Created successfully!!")
except :
    print("Table aleady Created!!")
y=1
while y == 1 :
    choice = int(input("\n1.Add Data  2.Delete Data  3.Update Data  4.Search  Data  5.Display Data : "))
    if choice == 1 :
        adddata()
    elif choice == 2 :
        deldata(conn)
    elif choice == 3 :
        updatedata(conn)
    elif choice == 4 :
        searchdata(conn)
    elif choice == 5 :
        disdata(conn)
    else :
        print("choose appropiate choice!!")
    y = int(input("\n1.continue  2.Exit : "))
conn.close()
