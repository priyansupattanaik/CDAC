class Book:
    def __init__(self, book_id, book_name, book_author, book_price):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_price = book_price

book1 = Book(101, "The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book(102, "To Kill a Mockingbird", "Harper Lee", 7.99)
book3 = Book(103, "1984", "George Orwell", 8.99)
book4 = Book(104, "Pride and Prejudice", "Jane Austen", 9.99)
book5 = Book(105, "The Catcher in the Rye", "J.D. Salinger", 6.99)

def display_book_details(book):
        print("Book ID:", book.book_id)
        print("Book Name:", book.book_name)
        print("Book Author:", book.book_author)
        print("Book Price: $", format(book.book_price, ".2f"))

def add_book(book_list, book):
    book_list.append(book)

def remove_book(book_list, book_id):
    for book in book_list:
        if book.book_id == book_id:
            book_list.remove(book)
            return True
    return False


def list_books(book_list):
    if not book_list:
        print("No books available.")
        return
    for book in book_list:
        display_book_details(book)
        print("-" * 30)
        print()


def main():
    book_list = [book1, book2, book3, book4, book5]
    print("Welcome to the Book Management System!")

    while True:
        print("\nChoose an option:")
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Remove a book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            list_books(book_list)

        elif choice == "2":
            try:
                new_id = int(input("Enter Book ID: ").strip())
                new_name = input("Enter Book Name: ").strip()
                new_author = input("Enter Book Author: ").strip()
                new_price = float(input("Enter Book Price: ").strip())
                add_book(book_list, Book(new_id, new_name, new_author, new_price))
                print("Book added successfully.")
            except ValueError:
                print("Invalid input. Book ID must be integer and price must be numeric.")

        elif choice == "3":
            try:
                remove_id = int(input("Enter Book ID to remove: ").strip())
                if remove_book(book_list, remove_id):
                    print("Book removed successfully.")
                else:
                    print("Book ID not found.")
            except ValueError:
                print("Invalid input. Book ID must be integer.")

        elif choice == "4":
            print("Exiting Book Management System.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
        
