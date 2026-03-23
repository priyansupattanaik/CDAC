import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="brucewayne")
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
cursor.execute("USE student_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
""")

students_data = [
    ('A', 22, 'Data Science'),
    ('B', 24, 'Python'),
    ('C', 23, 'AI'),
    ('D', 25, 'ML'),
    ('E', 22, 'SQL')
]

cursor.executemany("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)", students_data)
conn.commit()

print("All Students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE students SET course='Deep Learning' WHERE name='B'")
conn.commit()

cursor.execute("DELETE FROM students WHERE id=3")
conn.commit()

name = 'A'
cursor.execute("SELECT * FROM students WHERE name=%s", (name,))
print("\nSearch Result:")
print(cursor.fetchall())

cursor.close()
conn.close()