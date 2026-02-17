import mysql.connector

try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="newera")
    # connection.autocommit = True
    myCursor = connection.cursor()

    query = "INSERT INTO students (id, name,surname, phone) VALUES (%s, %s,%s, %s)"
    
    data = [
        (3,"Nikitavs",'vyas', "9988998899"),
        (4,"Bita",'patel',  "9988998899")
    ]

    myCursor.executemany(query, data)
    print(myCursor.rowcount, "New Record(s) Created")


except mysql.connector.Error as err:
    print("Error:", err)
