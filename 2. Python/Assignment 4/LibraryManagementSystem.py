class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def getDetails(self):
        return f"Title: {self.title}, Author: {self.author}"

class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    
    def getDetails(self):
        return f"{super().getDetails()}, Pages: {self.pages} (Printed Book)"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def getDetails(self):
        return f"{super().getDetails()}, File Size: {self.file_size}"


books = [
    PrintedBook("The Great Gatsby", "F. Scott Fitzgerald", 180),
    EBook("Python Programming", "John Doe", 5.2),
    PrintedBook("1984", "George Orwell", 328),
    EBook("Clean Code", "Robert Martin", 3.8)
]

for book in books:
    print(book.getDetails())