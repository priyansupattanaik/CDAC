# Create an application for library management system using instance,
# static/class and local variables. Also use instance, class and static methods.


class Book:
    total_books = 0

    def __init__(self, title, author, year):
        self.title = title.strip()
        self.author = author.strip()
        self.year = year.strip()
        Book.total_books += 1

    def display_info(self):
        info = f"Title: {self.title} | Author: {self.author} | Year: {self.year}"
        print(info)

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_year(year_text):
        return year_text.isdigit() and len(year_text) == 4


class Library:
    library_name = "Library"
    books = []

    @classmethod
    def add_book(cls, book):
        cls.books.append(book)

    @classmethod
    def set_library_name(cls, name):
        if name.strip():
            cls.library_name = name.strip()

    @staticmethod
    def display_menu():
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Display Total Book Count")
        print("4. Change Library Name")
        print("5. Exit")

    @staticmethod
    def display_books():
        if not Library.books:
            print("No books in the library.")
            return

        print(f"\nBooks in {Library.library_name}:")
        for index, book in enumerate(Library.books, start=1):
            print(f"{index}. ", end="")
            book.display_info()


def run_library_app():
    Library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "1925"))
    Library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "1960"))
    Library.add_book(Book("1984", "George Orwell", "1949"))

    while True:
        Library.display_menu()
        choice = input("Enter your choice: ").strip()  
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year = input("Enter publication year (YYYY): ").strip()

            if not title or not author:
                print("Title and author cannot be empty.")
                continue

            if not Book.is_valid_year(year):
                print("Invalid year. Please enter a 4-digit year.")
                continue

            new_book = Book(title, author, year)
            Library.add_book(new_book)
            print("Book added successfully.")

        elif choice == "2":
            Library.display_books()

        elif choice == "3":
            count = Book.get_total_books()  
            print(f"Total books created: {count}")

        elif choice == "4":
            new_name = input("Enter new library name: ").strip()
            Library.set_library_name(new_name)
            print(f"Library name updated to: {Library.library_name}")

        elif choice == "5":
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    run_library_app()