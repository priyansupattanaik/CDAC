import sys
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        database="quiz_system",
        user="root",
        password="brucewayne"
    )
    cursor = con.cursor()
    cursor.execute("DESCRIBE results")
    print("RESULTS SCHEMA:")
    for row in cursor.fetchall():
        print(row)
        
    cursor.execute("DESCRIBE users")
    print("\nUSERS SCHEMA:")
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print("ERROR:", e)
