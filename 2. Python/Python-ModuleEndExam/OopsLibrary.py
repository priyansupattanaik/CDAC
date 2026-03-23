#OOPS Library

import re
from abc import ABC, abstractmethod


class InvalidISBNError(Exception): pass
class BookAlreadyIssuedError(Exception): pass
class InvalidEmailError(Exception): pass


class LibraryItem(ABC):
    def __init__(self, title, author, year):
        self.__title  = title
        self.__author = author
        self.__year   = year

    def get_title(self):  return self.__title
    def get_author(self): return self.__author
    def get_year(self):   return self.__year

    @abstractmethod
    def display_info(self): pass

    @abstractmethod
    def get_fine(self, days): pass


class Book(LibraryItem):
    def __init__(self, title, author, year, isbn, genre):
        super().__init__(title, author, year)
        if not re.fullmatch(r'\d{3}-\d{10}', isbn):
            raise InvalidISBNError("ISBN must be like 978-0061965012")
        self.__isbn      = isbn
        self.__genre     = genre
        self.__is_issued = False

    def get_isbn(self):  return self.__isbn
    def get_genre(self):  return self.__genre
    def is_issued(self): return self.__is_issued

    def set_genre(self, g): self.__genre = g

    def issue_book(self):
        if self.__is_issued:
            raise BookAlreadyIssuedError(f"'{self.get_title()}' is already issued")
        self.__is_issued = True

    def return_book(self):
        self.__is_issued = False

    def display_info(self):
        status = "Issued" if self.__is_issued else "Available"
        print(f"  {self.__isbn} | {self.get_title()} | {self.get_author()} | {self.__genre} | {status}")

    def get_fine(self, days):
        return days * 2


class Magazine(LibraryItem):
    def __init__(self, title, publisher, year, issue_no):
        super().__init__(title, publisher, year)
        self.__issue_no = issue_no

    def display_info(self):
        print(f"  {self.get_title()} | {self.get_author()} | Issue: {self.__issue_no} | {self.get_year()}")

    def get_fine(self, days):
        return days * 1


class Member:
    def __init__(self, name, email, member_id):
        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
            raise InvalidEmailError("Invalid email")
        self.__name      = name
        self.__email     = email
        self.__member_id = member_id

    def get_member_id(self): return self.__member_id

    def display_info(self):
        print(f"  {self.__member_id} | {self.__name} | {self.__email}")


books     = {}
magazines = {}
members   = {}


def add_book():
    try:
        title  = input("Enter title: ")
        author = input("Enter author: ")
        year   = input("Enter year: ")
        isbn   = input("Enter ISBN (978-0061965012): ")
        genre  = input("Enter genre: ")
        if isbn in books:
            print("Book already exists")
            return
        b = Book(title, author, year, isbn, genre)
        books[isbn] = b
        print("Book added successfully")
    except (InvalidISBNError, ValueError) as e:
        print("Error:", e)
    finally:
        print("--- done ---")


def display_all_books():
    if not books:
        print("No books found")
        return
    for b in books.values():
        b.display_info()


def search_book():
    isbn = input("Enter ISBN: ")
    if isbn in books:
        books[isbn].display_info()
    else:
        print("Book not found")


def issue_book():
    try:
        isbn = input("Enter ISBN: ")
        if isbn not in books:
            print("Book not found")
            return
        books[isbn].issue_book()
        print("Issued successfully")
    except BookAlreadyIssuedError as e:
        print("Error:", e)


def return_book():
    isbn = input("Enter ISBN: ")
    if isbn not in books:
        print("Book not found")
        return
    days = int(input("Overdue days (0 if on time): "))
    books[isbn].return_book()
    print(f"Returned. Fine: Rs.{books[isbn].get_fine(days)}")


def count_books():
    issued = sum(1 for b in books.values() if b.is_issued())
    print(f"Total: {len(books)}  Issued: {issued}  Available: {len(books) - issued}")


def delete_book():
    isbn = input("Enter ISBN: ")
    if isbn in books:
        books.pop(isbn)
        print("Deleted")
    else:
        print("Book not found")


def add_member():
    try:
        name  = input("Enter name: ")
        email = input("Enter email: ")
        mid   = input("Enter member ID (M001): ")
        if mid in members:
            print("Member ID already exists")
            return
        m = Member(name, email, mid)
        members[mid] = m
        print("Member added successfully")
    except (InvalidEmailError, ValueError) as e:
        print("Error:", e)
    finally:
        print("--- done ---")


def display_all_members():
    if not members:
        print("No members found")
        return
    for m in members.values():
        m.display_info()


def add_magazine():
    title = input("Enter title: ")
    pub   = input("Enter publisher: ")
    year  = input("Enter year: ")
    issue = input("Enter issue number: ")
    key   = f"{title}-{issue}"
    m = Magazine(title, pub, year, issue)
    magazines[key] = m
    print("Magazine added successfully")


def display_all_magazines():
    if not magazines:
        print("No magazines found")
        return
    for m in magazines.values():
        m.display_info()


# sample data
books['978-0061965012'] = Book("Atomic Habits",    "James Clear",         2018, "978-0061965012", "Self-Help")
books['978-0743273565'] = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0743273565", "Fiction")
books['978-0201633610'] = Book("Design Patterns",  "Gang of Four",        1994, "978-0201633610", "Technology")
magazines['TimesIndia-101'] = Magazine("Times India", "Bennett Coleman", 2024, 101)
members['M001'] = Member("Ravi Sharma",  "ravi@gmail.com",  "M001")
members['M002'] = Member("Anita Mehta",  "anita@yahoo.com", "M002")


while True:
    print("\n===== Library System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Count Books")
    print("7. Delete Book")
    print("8. Add Magazine")
    print("9. Display Magazines")
    print("10. Add Member")
    print("11. Display Members")
    print("12. Exit")
    print("==========================")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter a number")
        continue

    if   choice == 1:  add_book()
    elif choice == 2:  display_all_books()
    elif choice == 3:  search_book()
    elif choice == 4:  issue_book()
    elif choice == 5:  return_book()
    elif choice == 6:  count_books()
    elif choice == 7:  delete_book()
    elif choice == 8:  add_magazine()
    elif choice == 9:  display_all_magazines()
    elif choice == 10: add_member()
    elif choice == 11: display_all_members()
    elif choice == 12:
        print("Goodbye!")
        break
    else:
        print("Invalid choice")