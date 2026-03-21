import mysql.connector

print("Connecting to the database...")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="brucewayne"
)

if conn.is_connected():
    print("Connected to the database")

cursor = conn.cursor() # Create a cursor object to interact with the database
cursor.execute("CREATE DATABASE IF NOT EXISTS testdb2")
print("Database testdb2")

cursor.execute("USE testdb2")

# create_tbl = """
# CREATE TABLE IF NOT EXISTS employee (
#     id     INT AUTO_INCREMENT PRIMARY KEY,
#     name   VARCHAR(255),
#     age    INT NOT NULL,
#     department VARCHAR(255)
#     );
#     """
# cursor.execute(create_tbl)
# print("Table 'employee' created successfully")
cursor.close()

query = "INSERT INTO employee (name, age, department) VALUES (%s, %s, %s)"

values = [
    ("C", 35, "Management"),
    ("B", 34, "MANAGEMENT"),
    ("A", 29, "HR"),
]

cursor = conn.cursor()

for entry in values:
    cursor.execute(query, entry)
    print(f"Inserted: {entry[0]}")

conn.commit()

print("Verifying inserted data:")
cursor.execute("SELECT * FROM employee")
results = cursor.fetchall()

for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Department: {row[3]}")

cursor.close()
conn.close()
print("Database connection closed")