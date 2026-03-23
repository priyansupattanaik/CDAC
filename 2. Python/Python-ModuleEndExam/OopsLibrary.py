import re
from abc import ABC, abstractmethod


# custom exceptions
class InvalidISBNError(Exception):
    pass

class BookAlreadyIssuedError(Exception):
    pass

class BookNotAvailableError(Exception):
    pass

class InvalidEmailError(Exception):
    pass


# abstract base class
class LibraryItem(ABC):

    def __init__(self, title, author, year):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if not str(year).isdigit() or int(year) < 1800 or int(year) > 2025:
            raise ValueError("Year must be between 1800 and 2025")
        self.__title  = title.strip()
        self.__author = author.strip()
        self.__year   = int(year)

    def get_title(self):  return self.__title
    def get_author(self): return self.__author
    def get_year(self):   return self.__year

    def set_title(self, t):
        if not t.strip():
            raise ValueError("Title cannot be empty")
        self.__title = t.strip()

    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def get_fine(self, days):
        pass


# Book class
class Book(LibraryItem):

    def __init__(self, title, author, year, isbn, genre):
        super().__init__(title, author, year)
        if not re.fullmatch(r'\d{3}-\d{10}', isbn):
            raise InvalidISBNError("ISBN format must be like 978-0061965012")
        self.__isbn      = isbn
        self.__genre     = genre
        self.__is_issued = False

    def get_isbn(self):  return self.__isbn
    def get_genre(self): return self.__genre
    def is_issued(self): return self.__is_issued

    def issue_book(self):
        if self.__is_issued:
            raise BookAlreadyIssuedError(f"'{self.get_title()}' is already issued")
        self.__is_issued = True

    def return_book(self):
        if not self.__is_issued:
            raise BookNotAvailableError(f"'{self.get_title()}' was not issued")
        self.__is_issued = False

    def display_info(self):
        status = "Issued" if self.__is_issued else "Available"
        print(f"  ISBN: {self.__isbn}  Title: {self.get_title()}  Author: {self.get_author()}")
        print(f"  Year: {self.get_year()}  Genre: {self.__genre}  Status: {status}")

    def get_fine(self, days):
        return days * 2


# Magazine class
class Magazine(LibraryItem):

    def __init__(self, title, publisher, year, issue_no):
        super().__init__(title, publisher, year)
        if not str(issue_no).isdigit() or int(issue_no) <= 0:
            raise ValueError("Issue number must be positive")
        self.__issue_no = int(issue_no)

    def get_issue_no(self): return self.__issue_no

    def display_info(self):
        print(f"  Title: {self.get_title()}  Publisher: {self.get_author()}")
        print(f"  Year: {self.get_year()}  Issue No: {self.__issue_no}")

    def get_fine(self, days):
        return days * 1


# Member class
class Member:

    def __init__(self, name, email, member_id):
        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
            raise InvalidEmailError("Invalid email format")
        if not re.fullmatch(r'M\d{3}', member_id):
            raise ValueError("Member ID must be like M001")
        self.__name      = name
        self.__email     = email
        self.__member_id = member_id

    def get_name(self):      return self.__name
    def get_email(self):     return self.__email
    def get_member_id(self): return self.__member_id

    def display_info(self):
        print(f"  {self.__member_id}  {self.__name}  {self.__email}")


# dictionaries to store data
books     = {}
magazines = {}
members   = {}


# book functions
def add_book():
    try:
        title  = input("Enter title: ")
        author = input("Enter author: ")
        year   = input("Enter year: ")
        isbn   = input("Enter ISBN (978-0061965012): ")
        genre  = input("Enter genre: ")
        if isbn in books:
            print("Book with this ISBN already exists")
            return
        b = Book(title, author, year, isbn, genre)
        books[b.get_isbn()] = b
        print("Book added successfully")
    except (InvalidISBNError, ValueError) as e:
        print("Error:", e)
    finally:
        print("--- done ---")


def display_all_books():
    if not books:
        print("No books found")
        return
    print("\n--- All Books ---")
    for b in books.values():
        b.display_info()
        print()


def search_book():
    isbn = input("Enter ISBN: ")
    if isbn in books:
        books[isbn].display_info()
    else:
        print("Book not found")


def issue_book():
    try:
        isbn = input("Enter ISBN to issue: ")
        if isbn not in books:
            print("Book not found")
            return
        books[isbn].issue_book()
        print("Book issued successfully")
    except BookAlreadyIssuedError as e:
        print("Error:", e)


def return_book():
    try:
        isbn = input("Enter ISBN to return: ")
        if isbn not in books:
            print("Book not found")
            return
        days = int(input("Enter overdue days (0 if on time): "))
        books[isbn].return_book()
        fine = books[isbn].get_fine(days)
        print(f"Book returned. Fine: Rs.{fine}")
    except (BookNotAvailableError, ValueError) as e:
        print("Error:", e)


def calculate_fine():
    isbn = input("Enter ISBN: ")
    if isbn not in books:
        print("Book not found")
        return
    try:
        days = int(input("Enter overdue days: "))
        print(f"Fine: Rs.{books[isbn].get_fine(days)}")
    except ValueError:
        print("Enter a valid number")


def sort_books_by_title():
    if not books:
        print("No books found")
        return
    sorted_list = sorted(books.values(), key=lambda b: b.get_title())
    print("\nBooks sorted by title:")
    for b in sorted_list:
        b.display_info()
        print()


def available_books():
    result = {isbn: b for isbn, b in books.items() if not b.is_issued()}
    if not result:
        print("No books available right now")
        return
    print("\nAvailable Books:")
    for b in result.values():
        b.display_info()
        print()


def count_books():
    total  = len(books)
    issued = sum(1 for b in books.values() if b.is_issued())
    print(f"Total: {total}  Issued: {issued}  Available: {total - issued}")


def delete_book():
    isbn = input("Enter ISBN to delete: ")
    if isbn in books:
        books.pop(isbn)
        print("Book deleted successfully")
    else:
        print("Book not found")


# magazine functions
def add_magazine():
    try:
        title  = input("Enter magazine title: ")
        pub    = input("Enter publisher: ")
        year   = input("Enter year: ")
        issue  = input("Enter issue number: ")
        key    = f"{title}-{issue}"
        if key in magazines:
            print("Magazine already exists")
            return
        m = Magazine(title, pub, year, issue)
        magazines[key] = m
        print("Magazine added successfully")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("--- done ---")


def display_all_magazines():
    if not magazines:
        print("No magazines found")
        return
    print("\n--- All Magazines ---")
    for m in magazines.values():
        m.display_info()
        print()


# member functions
def add_member():
    try:
        name  = input("Enter name: ")
        email = input("Enter email: ")
        mid   = input("Enter member ID (M001): ")
        if mid in members:
            print("Member ID already exists")
            return
        m = Member(name, email, mid)
        members[m.get_member_id()] = m
        print("Member added successfully")
    except (InvalidEmailError, ValueError) as e:
        print("Error:", e)
    finally:
        print("--- done ---")


def display_all_members():
    if not members:
        print("No members found")
        return
    print("\n--- All Members ---")
    for m in members.values():
        m.display_info()


# sample data
books['978-0061965012'] = Book("Atomic Habits",    "James Clear",         2018, "978-0061965012", "Self-Help")
books['978-0743273565'] = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0743273565", "Fiction")
books['978-0201633610'] = Book("Design Patterns",  "Gang of Four",        1994, "978-0201633610", "Technology")
magazines['TimesIndia-101'] = Magazine("Times India", "Bennett Coleman", 2024, 101)
members['M001'] = Member("Ravi Sharma",  "ravi@gmail.com",  "M001")
members['M002'] = Member("Anita Mehta",  "anita@yahoo.com", "M002")


# main menu
while True:
    print("\n===== Library Management System =====")
    print("--- Books ---")
    print("1.  Add Book")
    print("2.  Display All Books")
    print("3.  Search Book")
    print("4.  Issue Book")
    print("5.  Return Book")
    print("6.  Calculate Fine")
    print("7.  Sort Books by Title")
    print("8.  Show Available Books")
    print("9.  Count Books")
    print("10. Delete Book")
    print("--- Magazines ---")
    print("11. Add Magazine")
    print("12. Display All Magazines")
    print("--- Members ---")
    print("13. Add Member")
    print("14. Display All Members")
    print("15. Exit")
    print("=====================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if   choice == 1:  add_book()
    elif choice == 2:  display_all_books()
    elif choice == 3:  search_book()
    elif choice == 4:  issue_book()
    elif choice == 5:  return_book()
    elif choice == 6:  calculate_fine()
    elif choice == 7:  sort_books_by_title()
    elif choice == 8:  available_books()
    elif choice == 9:  count_books()
    elif choice == 10: delete_book()
    elif choice == 11: add_magazine()
    elif choice == 12: display_all_magazines()
    elif choice == 13: add_member()
    elif choice == 14: display_all_members()
    elif choice == 15:
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")