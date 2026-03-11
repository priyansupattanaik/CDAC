import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Book {
    private String title;
    private String author;
    private String publisher;
    private String isbn;
    private int year;
    private double price;
    private int quantity;

    public Book() {
        this.title = "Unknown";
        this.author = "Unknown";
        this.publisher = "Unknown";
        this.isbn = "000-0000000000";
        this.year = 0;
        this.price = 0.0;
        this.quantity = 0;
    }

    public Book(String title, String author, String publisher, String isbn, int year, double price, int quantity) {
        this.title = title;
        this.author = author;
        this.publisher = publisher;
        this.isbn = isbn;
        this.year = year;
        this.price = price;
        this.quantity = quantity;
    }

    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public String getPublisher() { return publisher; }
    public String getIsbn() { return isbn; }
    public int getYear() { return year; }
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }

    public void setTitle(String title) { this.title = title; }
    public void setAuthor(String author) { this.author = author; }
    public void setPublisher(String publisher) { this.publisher = publisher; }
    public void setIsbn(String isbn) { this.isbn = isbn; }
    public void setYear(int year) { this.year = year; }
    public void setPrice(double price) { this.price = price; }
    public void setQuantity(int quantity) { this.quantity = quantity; }


    public void increaseQuantity(int quantity) {
        if (quantity > 0) {
            this.quantity += quantity;
            System.out.println("Quantity increased. New quantity: " + this.quantity);
        } else {
            System.out.println("Increase amount must be greater than zero.");
        }
    }

    public void decreaseQuantity(int quantity) {
        if (quantity > 0 && quantity <= this.quantity) {
            this.quantity -= quantity;
            System.out.println("Quantity decreased. New quantity: " + this.quantity);
        } else if (quantity > this.quantity) {
            System.out.println("Not enough stock.");
        } else {
            System.out.println("Decrease amount must be greater than zero.");
        }
    }

    public double getInventoryValue() {
        return price * quantity;
    }

    public void displayBookInfo() {
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Publisher: " + publisher);
        System.out.println("ISBN: " + isbn);
        System.out.println("Year: " + year);
        System.out.println("Price: $" + price);
        System.out.println("Quantity: " + quantity);
        System.out.println("Inventory Value: $" + getInventoryValue());
    }
}



public class BookManager {
    private static List<Book> inventory = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        inventory.add(new Book("Clean Code", "Robert C. Martin", "Prentice Hall", "9734567865", 2008, 657, 10));
        inventory.add(new Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "Addison-Wesley", "974545555555", 1999, 498, 7));
        inventory.add(new Book("Introduction to Java", "Daniel Liang", "Pearson", "978454656446", 2021, 935, 15));

        int choice;
        do {
            printMenu();
            System.out.print("Enter choice: ");
            choice = scanner.nextInt();
            scanner.nextLine();
            if (choice == 1) viewAllBooks();
            else if (choice == 2) addBook();
            else if (choice == 3) increaseStock();
            else if (choice == 4) decreaseStock();
            else if (choice == 5) viewInventoryValue();
            else if (choice == 6) searchBook();
            else if (choice == 0) System.out.println("Goodbye!");
            else System.out.println("Invalid option. Try again.");
        } while (choice != 0);
        scanner.close();
    }

    private static void printMenu() {
        System.out.println("\nBook Inventory System");
        System.out.println("1. View All Books");
        System.out.println("2. Add New Book");
        System.out.println("3. Increase Book Quantity");
        System.out.println("4. Decrease Book Quantity");
        System.out.println("5. View Total Inventory Value");
        System.out.println("6. Search Book by Title");
        System.out.println("0. Exit");
    }


    private static void viewAllBooks() {
        if (inventory.isEmpty()) {
            System.out.println("No books in inventory.");
            return;
        }
        for (int i = 0; i < inventory.size(); i++) {
            System.out.println("Book #" + (i + 1));
            inventory.get(i).displayBookInfo();
        }
    }


    private static void addBook() {
        System.out.println("Add New Book");
        System.out.print("Title: "); String title = scanner.nextLine();
        System.out.print("Author: "); String author = scanner.nextLine();
        System.out.print("Publisher: "); String publisher = scanner.nextLine();
        System.out.print("ISBN: "); String isbn = scanner.nextLine();
        System.out.print("Year: "); int year = scanner.nextInt();
        System.out.print("Price: "); double price = scanner.nextDouble();
        System.out.print("Quantity: "); int quantity = scanner.nextInt();
        scanner.nextLine();
        Book newBook = new Book(title, author, publisher, isbn, year, price, quantity);
        inventory.add(newBook);
        System.out.println("Book added!");
        newBook.displayBookInfo();
    }


    private static void increaseStock() {
        System.out.println("Increase Book Quantity");
        Book book = selectBook();
        if (book == null) return;
        System.out.print("Units to add: ");
        int qty = scanner.nextInt();
        scanner.nextLine();
        book.increaseQuantity(qty);
    }


    private static void decreaseStock() {
        System.out.println("Decrease Book Quantity");
        Book book = selectBook();
        if (book == null) return;
        System.out.print("Units to remove: ");
        int qty = scanner.nextInt();
        scanner.nextLine();
        book.decreaseQuantity(qty);
    }


    private static void viewInventoryValue() {
        System.out.println("Inventory Value Report");
        double totalValue = 0;
        for (Book book : inventory) {
            double val = book.getInventoryValue();
            System.out.println(book.getTitle() + " - " + val + " (Qty: " + book.getQuantity() + ")");
            totalValue += val;
        }
        System.out.println("Total Inventory Value: " + totalValue);
    }


    private static void searchBook() {
        System.out.print("Enter title to search: ");
        String keyword = scanner.nextLine().toLowerCase();
        boolean found = false;
        for (Book book : inventory) {
            if (book.getTitle().toLowerCase().contains(keyword)) {
                book.displayBookInfo();
                found = true;
            }
        }
        if (!found) System.out.println("No book found with that title.");
    }


    private static Book selectBook() {
        if (inventory.isEmpty()) {
            System.out.println("No books available.");
            return null;
        }
        for (int i = 0; i < inventory.size(); i++) {
            System.out.println((i + 1) + ". " + inventory.get(i).getTitle());
        }
        System.out.print("Select book number: ");
        int index = scanner.nextInt() - 1;
        scanner.nextLine();
        if (index < 0 || index >= inventory.size()) {
            System.out.println("Invalid selection.");
            return null;
        }
        return inventory.get(index);
    }
}