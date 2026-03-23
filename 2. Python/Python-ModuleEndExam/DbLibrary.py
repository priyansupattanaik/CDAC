import mysql.connector

conn   = mysql.connector.connect(host="localhost", user="root", password="brucewayne")
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
cursor.execute("USE library_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    title    VARCHAR(150),
    author   VARCHAR(100),
    genre    VARCHAR(50),
    price    FLOAT,
    quantity INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    member_id VARCHAR(10) PRIMARY KEY,
    name      VARCHAR(100),
    email     VARCHAR(100),
    phone     VARCHAR(15)
)
""")
conn.commit()


# book functions
def add_book():
    title    = input("Enter title: ")
    author   = input("Enter author: ")
    genre    = input("Enter genre: ")
    price    = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cursor.execute(
        "INSERT INTO books (title, author, genre, price, quantity) VALUES (%s, %s, %s, %s, %s)",
        (title, author, genre, price, quantity)
    )
    conn.commit()
    print("Book added successfully!")


def view_all_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    if not rows:
        print("No books found")
        return
    print("\n--- All Books ---")
    print(f"{'ID':<5} {'Title':<25} {'Author':<20} {'Genre':<15} {'Price':<10} Qty")
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<25} {row[2]:<20} {row[3]:<15} {row[4]:<10} {row[5]}")


def search_book():
    title = input("Enter title to search: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
    rows = cursor.fetchall()
    if not rows:
        print("No books found")
        return
    for row in rows:
        print(row)


def update_price():
    bid   = int(input("Enter book ID: "))
    price = float(input("Enter new price: "))
    cursor.execute("UPDATE books SET price=%s WHERE id=%s", (price, bid))
    conn.commit()
    if cursor.rowcount == 0:
        print("Book not found")
    else:
        print("Price updated!")


def update_quantity():
    bid = int(input("Enter book ID: "))
    qty = int(input("Enter quantity to add: "))
    cursor.execute("UPDATE books SET quantity = quantity + %s WHERE id=%s", (qty, bid))
    conn.commit()
    print("Quantity updated!")


def delete_book():
    bid = int(input("Enter book ID to delete: "))
    cursor.execute("DELETE FROM books WHERE id=%s", (bid,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Book not found")
    else:
        print("Book deleted!")


def most_expensive():
    cursor.execute("SELECT * FROM books ORDER BY price DESC LIMIT 1")
    print("Most expensive book:")
    print(cursor.fetchone())


def books_by_genre():
    genre = input("Enter genre: ")
    cursor.execute("SELECT * FROM books WHERE genre=%s", (genre,))
    rows = cursor.fetchall()
    if not rows:
        print("No books in this genre")
        return
    for row in rows:
        print(row)


def count_by_genre():
    cursor.execute("SELECT genre, COUNT(*) FROM books GROUP BY genre")
    print("Books per genre:")
    for row in cursor.fetchall():
        print(row)


def total_stock_value():
    cursor.execute("SELECT SUM(price * quantity) FROM books")
    result = cursor.fetchone()[0]
    print(f"Total stock value: Rs.{result}")


# member functions
def add_member():
    mid   = input("Enter member ID (M001): ")
    name  = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    cursor.execute(
        "INSERT INTO members (member_id, name, email, phone) VALUES (%s, %s, %s, %s)",
        (mid, name, email, phone)
    )
    conn.commit()
    print("Member added successfully!")


def view_all_members():
    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()
    if not rows:
        print("No members found")
        return
    print("\n--- All Members ---")
    for row in rows:
        print(row)


def delete_member():
    mid = input("Enter member ID to delete: ")
    cursor.execute("DELETE FROM members WHERE member_id=%s", (mid,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Member not found")
    else:
        print("Member deleted!")


# main menu
while True:
    print("\n===== Library DB System =====")
    print("--- Books ---")
    print("1.  Add Book")
    print("2.  View All Books")
    print("3.  Search Book")
    print("4.  Update Price")
    print("5.  Update Quantity")
    print("6.  Delete Book")
    print("7.  Most Expensive Book")
    print("8.  Books by Genre")
    print("9.  Count by Genre")
    print("10. Total Stock Value")
    print("--- Members ---")
    print("11. Add Member")
    print("12. View All Members")
    print("13. Delete Member")
    print("14. Exit")
    print("=============================")

    choice = int(input("Enter your choice: "))

    if   choice == 1:  add_book()
    elif choice == 2:  view_all_books()
    elif choice == 3:  search_book()
    elif choice == 4:  update_price()
    elif choice == 5:  update_quantity()
    elif choice == 6:  delete_book()
    elif choice == 7:  most_expensive()
    elif choice == 8:  books_by_genre()
    elif choice == 9:  count_by_genre()
    elif choice == 10: total_stock_value()
    elif choice == 11: add_member()
    elif choice == 12: view_all_members()
    elif choice == 13: delete_member()
    elif choice == 14:
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

cursor.close()
conn.close()