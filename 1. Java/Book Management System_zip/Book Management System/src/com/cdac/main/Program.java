package com.cdac.main;

import java.util.Scanner;

import com.cdac.exceptions.BookNotFoundException;
import com.cdac.exceptions.DuplicateBookIdException;
import com.cdac.exceptions.InvalidBookDataException;
import com.cdac.managers.BookManager;

public class Program {

    public static void main(String[] args) throws InvalidBookDataException, DuplicateBookIdException, BookNotFoundException {

        Scanner sc = new Scanner(System.in);
        BookManager manager = new BookManager();

        int choice;

        do {

            System.out.println("\n===== LIBRARY MANAGEMENT SYSTEM =====");
            System.out.println("1. Add Book");
            System.out.println("2. View All Books");
            System.out.println("3. Search Book");
            System.out.println("4. Update Book");
            System.out.println("5. Delete Book");
            System.out.println("6. Sort by Title");
            System.out.println("7. Sort by Author");
            System.out.println("8. Sort by Price");
            System.out.println("9. Sort by Rating");
            System.out.println("10. Sort by Publication Year");
            System.out.println("11. Exit");

            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {

                case 1: manager.addBook(); break;
                case 2: manager.viewBooks(); break;
                case 3: manager.searchBook(); break;
                case 4: manager.updateBook(); break;
                case 5: manager.deleteBook(); break;
                case 6: manager.sortByTitle(); break;
                case 7: manager.sortByAuthor(); break;
                case 8: manager.sortByPrice(); break;
                case 9: manager.sortByRating(); break;
                case 10: manager.sortByPublicationYear(); break;
                case 11: System.out.println("Exiting..."); break;
                default: System.out.println("Invalid choice");

            }

        } while (choice != 11);

        sc.close();
    }
}