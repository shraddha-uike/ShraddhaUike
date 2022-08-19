#To retrieve all records and columns from table
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

#Step 2 :
#Creating a cursor object using the cursor() method
cur = con.cursor()

#step 3:  Query fire
query="SELECT * FROM STUDENT"

#step 4: Query run use execute method of cursor
try:
    cur.execute(query)
except Exception :
    print("Query Error")
else:
    #Fetching all rows from the table
    result = cur.fetchall() #here result user defined object , hold all records in this object
    print(result) #here result object tuple type , means no changes the record
cur.close()
con.close()
