import pymysql
class School:
    def _init_(self): #constructor function
#STEP 1 :  create connection string python with mysqlserver
        __servername="localhost"  #private variable
        __username="root"
        __password=""
        __dbname="school_vedant" #dbname means database name
        try:
            self.con=pymysql.connect(_servername,username,password,_dbname)
            #con user defined object name
            #con object of connect()
        except Exception:
            print("Connection Error")
        else:
            print("Connection successfully")
            
    def _del_(self): #destructor function
        self.con.close()

    def insertrecord(self):
        #insert record
        en=int(input("Enter Enrollment no. : "))
        n=input("Enter Student Name ")  #varchar type in table=string
        a=int(input("Enter Age : "))
        c=input("Enter City :")
    #to insert data from front end (python's output screen) to backend(sqlserver)
    #the fire SQL Query
        query="INSERT INTO STUDENT(enroll,name,age,city)values(%s,%s,%s,%s)"  #%s means string
        val=(en,n,a,c) #val tuple variable
        #Create  cursor
        cur=self.con.cursor()
        #run insert query
        try:
            cur.execute(query,val)
        except:
            print("Query Error")
        else:
        #save in database  use commit()
            self.con.commit()
            print("Record Insert Successfully")
        cur.close() #close the cursor
    def menu(self):
        print("1. Insert Record \n 2. View Record \n 3. Search Record \n 4. Delete Record \n 5. Update Record \n 6. Exit")

#main program
s1=School() #here s1 object of class School ,call constructor automatic _init_()
while(True):
    s1.menu()
    ch=int(input("Enter Your choice : "))
    if(ch==1):
        s1.insertrecord()
    elif(ch==6):
        break #exit from loop
