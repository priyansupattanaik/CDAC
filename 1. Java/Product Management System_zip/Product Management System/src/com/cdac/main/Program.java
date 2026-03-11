package com.cdac.main;

import java.util.Scanner;
import com.cdac.exceptions.*;
import com.cdac.managers.ProductManager;

public class Program {

    public static void main(String[] args) throws DuplicateProductIdException, ProductNotFoundException, InvalidProductDataException{

        Scanner sc = new Scanner(System.in);
        ProductManager manager = new ProductManager();

        int choice;

        do {

            System.out.println("\n===== PRODUCT INVENTORY SYSTEM =====");
            System.out.println("1. Add Product");
            System.out.println("2. View All Products");
            System.out.println("3. Search Product by ID");
            System.out.println("4. Update Product");
            System.out.println("5. Delete Product");
            System.out.println("6. Sort by Name");
            System.out.println("7. Sort by Price");
            System.out.println("8. Sort by Quantity");
            System.out.println("9. Sort by Rating");
            System.out.println("10. Exit");

            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {

                case 1: manager.addProduct(); break;
                case 2: manager.viewProducts(); break;
                case 3: manager.searchProduct(); break;
                case 4: manager.updateProduct(); break;
                case 5: manager.deleteProduct(); break;
                case 6: manager.sortByName(); break;
                case 7: manager.sortByPrice(); break;
                case 8: manager.sortByQuantity(); break;
                case 9: manager.sortByRating(); break;
                case 10: System.out.println("Exiting..."); break;
                default: System.out.println("Invalid choice");

            }

        } while (choice != 10);

        sc.close();
    }
}