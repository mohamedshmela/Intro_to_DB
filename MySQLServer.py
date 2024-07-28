import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345shmela@sql"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

mycursor.close()
mydb.close()