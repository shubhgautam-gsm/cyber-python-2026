import mysql.connector

#STEP 2 CREATE TABLE IN DATABASE alratv_app
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="newera")

    myCursor = connection.cursor()
    query = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), phone INT(255))"
    result = myCursor.execute(query)
    print("Table Created")

    connection.close()
except Exception as err:
    print("Error is ", err)
