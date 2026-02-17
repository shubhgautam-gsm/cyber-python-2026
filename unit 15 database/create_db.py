import mysql.connector
#STEP 1 CREATE DATABSE AND CONNECT TO MYSQL
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="")
    print("Database Connected")
    myCursor = connection.cursor()
    query = "create database newera" 
    result = myCursor.execute(query) # run the command
    print("Database Created")

    connection.close()
except Exception as err:
    print("Error is ",err)