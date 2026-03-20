import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="brucewayne",
    database="test_db"
)

cursor = conn.cursor()

# Create table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     NAME VARCHAR(100),
#     AGE INT,
#     COURSE VARCHAR(100)
# )
# """)

# Insert data
query = "INSERT INTO students (NAME, AGE, COURSE) VALUES (%s, %s, %s)"
values = ("Amit", 24, "Python")

cursor.execute(query, values)
conn.commit()

print("Data Inserted Successfully")

cursor.close()
conn.close()