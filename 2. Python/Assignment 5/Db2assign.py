import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="brucewayne")
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS company_db")
cursor.execute("USE company_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT
)
""")
conn.commit()

while True:
    print("\n--- Employee Menu ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Highest Paid Employee")
    print("6. Count Employees per Department")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        dept = input("Enter department: ")
        salary = float(input("Enter salary: "))
        cursor.execute("INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)", (name, dept, salary))
        conn.commit()
        print("Employee added successfully!")

    elif choice == 2:
        cursor.execute("SELECT * FROM employee")
        for row in cursor.fetchall():
            print(row)

    elif choice == 3:
        emp_id = int(input("Enter employee ID: "))
        new_salary = float(input("Enter new salary: "))
        cursor.execute("UPDATE employee SET salary=%s WHERE emp_id=%s", (new_salary, emp_id))
        conn.commit()
        print("Salary updated!")

    elif choice == 4:
        emp_id = int(input("Enter employee ID to delete: "))
        cursor.execute("DELETE FROM employee WHERE emp_id=%s", (emp_id,))
        conn.commit()
        print("Employee deleted!")

    elif choice == 5:
        cursor.execute("SELECT * FROM employee ORDER BY salary DESC LIMIT 1")
        print("Highest Paid Employee:")
        print(cursor.fetchone())

    elif choice == 6:
        cursor.execute("SELECT department, COUNT(*) FROM employee GROUP BY department")
        print("Employees per Department:")
        for row in cursor.fetchall():
            print(row)

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

cursor.close()
conn.close()