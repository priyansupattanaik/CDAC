package com.cdac.managers;

import com.cdac.models.Book;
import com.cdac.exceptions.*;

import java.util.*;

public class BookManager extends LibraryOperations {

     ArrayList<Book> books = new ArrayList<>();
     
     public BookManager() {
    	 books.add(new Book(1, "ABC", "XY", 150.00, 9.8, 2000));
    	 books.add(new Book(3, "XYZ", "AB", 189.99, 8.2, 2013));
    	 books.add(new Book(5, "NMD", "NN", 100.99, 9.9, 2026));
    	 books.add(new Book(4, "AAC", "JK", 99.99, 5.4, 2002));
    	 books.add(new Book(2, "TVB", "LN", 199.99, 6.9, 2017));    	 
     }
     
     Scanner sc = new Scanner(System.in);

    @Override
    public void addBook() throws InvalidBookDataException, DuplicateBookIdException {

        try {

            System.out.print("Enter Book ID: ");
            int id = sc.nextInt();
            sc.nextLine();

            for (Book b : books) {
                if (b.getBookId() == id) {
                    throw new DuplicateBookIdException("Book ID already exists!");
                }
            }

            System.out.print("Enter Title: ");
            String title = sc.nextLine();
            
            System.out.print("Enter Author: ");
            String author = sc.nextLine();

            System.out.print("Enter Price: ");
            double price = sc.nextDouble();

            System.out.print("Enter Rating: ");
            double rating = sc.nextDouble();

            System.out.print("Enter Publication Year: ");
            int year = sc.nextInt();

            if (price < 0 || rating < 0) {
                throw new InvalidBookDataException("Price or Rating cannot be negative.");
            }

            Book book = new Book(id, title, author, price, rating, year);

            books.add(book);

            System.out.println("Book added successfully.");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public void viewBooks() {

        if (books.isEmpty()) {
            System.out.println("No books available.");
            return;
        }
//   books.stream().forEach(Book b:books -> System.out.println(b))
        for (Book b : books) {
            System.out.println(b);
        }
    }

    @Override
    public void searchBook() throws BookNotFoundException {

        try {

            System.out.print("Enter Book ID to search: ");
            int id = sc.nextInt();

            for (Book b : books) {
                if (b.getBookId() == id) {
                    System.out.println(b);
                    return;
                }
            }

            throw new BookNotFoundException("Book not found!");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public void updateBook() throws BookNotFoundException {

        try {

            System.out.print("Enter Book ID to update: ");
            int id = sc.nextInt();
            sc.nextLine();

            for (Book b : books) {

                if (b.getBookId() == id) {

                    System.out.print("Enter New Title: ");
                    b.setTitle(sc.nextLine());

                    System.out.print("Enter New Author: ");
                    b.setAuthor(sc.nextLine());

                    System.out.print("Enter New Price: ");
                    b.setPrice(sc.nextDouble());

                    System.out.print("Enter New Rating: ");
                    b.setRating(sc.nextDouble());

                    System.out.print("Enter New Publication Year: ");
                    b.setPublicationYear(sc.nextInt());

                    System.out.println("Book updated successfully.");
                    return;
                }
            }

            throw new BookNotFoundException("Book not found!");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public void deleteBook() throws BookNotFoundException{

        try {

            System.out.print("Enter Book ID to delete: ");
            int id = sc.nextInt();

            Iterator<Book> it = books.iterator();

            while (it.hasNext()) {

                Book b = it.next();

                if (b.getBookId() == id) {
                    it.remove();
                    System.out.println("Book deleted successfully.");
                    return;
                }
            }

            throw new BookNotFoundException("Book not found!");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

// EASIER WAY
//    public void deleteBook() {
//
//        try {
//
//            System.out.print("Enter Book ID to delete: ");
//            int id = sc.nextInt();
//
//            Book bookToDelete = null;
//
//            for (Book b : books) {
//                if (b.getBookId() == id) {
//                    bookToDelete = b;
//                    break;
//                }
//            }
//
//            if (bookToDelete == null) {
//                throw new BookNotFoundException("Book not found!");
//            }
//
//            books.remove(bookToDelete);
//
//            System.out.println("Book deleted successfully.");
//
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//        }
//    }
    
//    USING STREAM
    
//    public void deleteBook() {
//
//        try {
//
//            System.out.print("Enter Book ID to delete: ");
//            int id = sc.nextInt();
//
//            boolean removed = books.removeIf(b -> b.getBookId() == id);
    
//            books.stram().removeIF(b -> b.getBookId() == id);
//
//            if (!removed) {
//                throw new BookNotFoundException("Book not found!");
//            }
//
//            System.out.println("Book deleted successfully.");
//
//        } catch (Exception e) {
//            System.out.println(e.getMessage());
//        }
//    }
    

    @Override
    public void sortByTitle() {

        Collections.sort(books, (b1, b2) ->
                b1.getTitle().compareToIgnoreCase(b2.getTitle()));

        System.out.println("Sorted by Title.");
        viewBooks();
    }

//    USING STREAM
//    public void sortByTitle() {
//
//        System.out.println("Books sorted by Title:\n");
//
//        books.stream()
//             .sorted((b1, b2) -> b1.getTitle().compareToIgnoreCase(b2.getTitle()))
//             .forEach(System.out::println);
//    }
    
    @Override
    public void sortByAuthor() {

        Collections.sort(books, (b1, b2) ->
                b1.getAuthor().compareToIgnoreCase(b2.getAuthor()));
//        books.stream()
//        .sorted((b1, b2) -> Double.compare(b1.getPrice(), b2.getPrice()))
//        .forEach(System.out::println);

        System.out.println("Sorted by Author.");
        viewBooks();
    }

    @Override
    public void sortByPrice() {

        Collections.sort(books, (b1, b2) ->
                Double.compare(b1.getPrice(), b2.getPrice()));

        System.out.println("Sorted by Price.");
        viewBooks();
    }

    @Override
    public void sortByRating() {

        Collections.sort(books, (b1, b2) ->
                Double.compare(b2.getRating(), b1.getRating()));

        System.out.println("Sorted by Rating.");
        viewBooks();
    }

    @Override
    public void sortByPublicationYear() {

        Collections.sort(books, (b1, b2) ->
                Integer.compare(b1.getPublicationYear(), b2.getPublicationYear()));

        System.out.println("Sorted by Publication Year.");
        viewBooks();
    }
}