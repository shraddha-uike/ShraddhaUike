import pymysql
#create connection string python with mysqlserver
servername="localhost"
username="root"
password=""
dbname="school_vedant" #dbname means database name
try:
    con=pymysql.connect(servername,username,password,dbname) #con user defined object name

except Exception:
    print("Connection Error")
else:
    print("Connection successfully")

#create table and store in existing database
    #provide SQL :  1. DDL
    #SQL Query  : it is not a case sensitive
query="CREATE TABLE student(enroll int primary key,name varchar(30) not null,age int not null,city varchar(30))"
#Execute the query means run the query with the help of python
#create the cursor object using the inbuilt mrthod cursor()
cur=con.cursor() #create the cursor cur (connect table from connection string con)
#run the query use inbuilt method execute( ) of cursor method
try:
    cur.execute(query)
except Exception:
    print("Query Error")
else:
    print("Table create successfully")
