import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345shmela@sql"
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"an error occured: {e}")

finally:
    mycursor.close()
    mydb.close()
    print("my sql connection is closed")