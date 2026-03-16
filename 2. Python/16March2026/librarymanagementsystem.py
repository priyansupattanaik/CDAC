#Create a application for library management system using instance, static/class and local variables.
#Also use instance method, class method, static method.

class Book:
    def __init__(self, title, autho


class Books:
    @classmethod
    def __init__(cls, title, author, year):
        cls.title = title.strip()
        cls.author = author.strip()
        cls.year = year.strip()
        @staticmethod
        def display_info():
            print("Title:",Books.title)
            print("Author:",Books.author)
            print("Year:",Books.year)


class Library:
    books = []

    @classmethod
    def add_book(cls, book):
        cls.books.append(book)

    @staticmethod
    def display_books():
        if not Library.books:
            print("No books in the library.")
            return
        for book in Library.books:
            book.display_info()
            print("-" * 20)

print("Library Management System")
while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter publication year: ")
        book = Books(title, author, year)
        Library.add_book(book)
        print("Book added successfully.")
    elif choice == '2':
        Library.display_books()
    elif choice == '3':
        print("Exiting")
        break