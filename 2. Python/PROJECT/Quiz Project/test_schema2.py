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
    with open("schema.txt", "w") as f:
        f.write("RESULTS SCHEMA:\n")
        for row in cursor.fetchall():
            f.write(str(row) + "\n")
            
        cursor.execute("DESCRIBE users")
        f.write("\nUSERS SCHEMA:\n")
        for row in cursor.fetchall():
            f.write(str(row) + "\n")
except Exception as e:
    with open("schema.txt", "w") as f:
        f.write("ERROR: " + str(e))
