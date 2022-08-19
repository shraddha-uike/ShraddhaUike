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
