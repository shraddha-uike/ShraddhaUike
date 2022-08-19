#Insert record in table 
import pymysql
#STEP 1 :  create connection string python with mysqlserver
servername="localhost"
username="root"
password=""
dbname="school_vedant" #dbname means database name
try:
    con=pymysql.connect(servername,username,password,dbname) #con user defined object name
    #con object of connect()
except Exception:
    print("Connection Error")
else:
    print("Connection successfully")


#STEP 2 :  create the cursor
#create the cursor object using the inbuilt method cursor()
cur=con.cursor() #create the cursor object : cur (connect table from connectionstring con)
#cursor() inbuilt method of pymysql.connect()
#input from user on output screen on runtime
en=int(input("Enter Enrollment no. : "))
n=input("Enter Student Name : ")
a=int(input("Enter Age of student : "))
c=input("Enter City : ")

#step 3 : Query Fire :
#here to insert record in table : DML
query="INSERT INTO student(enroll,name,age,city)VALUES(%s,%s,%s,%s)"
#%s means string type data
#tuple variable : val
val=(en,n,a,c)
#step 4 Query run with the help of execute( ) , it is inbuilt method of cursor class
try:
    cur.execute(query,val)
except Exception:
    print("Query Error")
else:
    con.commit()  #to save data in table
    #commit() inbuilt method of connect()
    print("Record save successfully")
cur.close() #close cursor , close() inbuilt method of cursor
con.close() #close() connection , close() inbuilt of connect()
