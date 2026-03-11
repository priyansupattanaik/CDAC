package com.inventory.main;

import java.util.List;
import java.util.Scanner;

import com.inventory.exceptions.ProductException;
import com.inventory.managers.ProductManager;
import com.inventory.models.Product;

public class Program {
    
    private static Scanner sc = new Scanner(System.in);
    private static ProductManager productManager = new ProductManager();
    
    public static void main(String[] args) {
        int choice;
        
        // Welcome message from abstract class
        productManager.displayWelcomeMessage();
        
        do {
            displayMenu();
            try {
                choice = Integer.parseInt(sc.nextLine());
                
                switch (choice) {
                    case 1:
                        addProduct();
                        break;
                    case 2:
                        viewAllProducts();
                        break;
                    case 3:
                        searchProductById();
                        break;
                    case 4:
                        updateProduct();
                        break;
                    case 5:
                        deleteProduct();
                        break;
                    case 6:
                        productManager.sortProductsByName();
                        break;
                    case 7:
                        productManager.sortProductsByPrice();
                        break;
                    case 8:
                        productManager.sortProductsByQuantity();
                        break;
                    case 9:
                        productManager.sortProductsByRating();
                        break;
                    case 10:
                        searchByCategory();
                        break;
                    case 11:
                        filterByPrice();
                        break;
                    case 12:
                        System.out.println("Exiting the program. Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid choice! Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid number!");
                choice = 0;
            }
            
        } while (choice != 12);
        
        sc.close();
    }
    
    private static void displayMenu() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("PRODUCT INVENTORY MANAGEMENT SYSTEM");
        System.out.println("=".repeat(60));
        System.out.println("1. Add Product");
        System.out.println("2. View All Products");
        System.out.println("3. Search Product by ID");
        System.out.println("4. Update Product");
        System.out.println("5. Delete Product");
        System.out.println("6. Sort Products by Name");
        System.out.println("7. Sort Products by Price");
        System.out.println("8. Sort Products by Quantity");
        System.out.println("9. Sort Products by Rating");
        System.out.println("10. Search Products by Category");
        System.out.println("11. Filter Products by Price Range");
        System.out.println("12. Exit");
        System.out.println("=".repeat(60));
        System.out.print("Enter your choice: ");
    }
    
    private static void addProduct() {
        try {
            System.out.println("\n--- Add New Product ---");
            
            System.out.print("Enter Product ID: ");
            int id = Integer.parseInt(sc.nextLine());
            
            System.out.print("Enter Product Name: ");
            String name = sc.nextLine();
            
            System.out.print("Enter Category: ");
            String category = sc.nextLine();
            
            System.out.print("Enter Price: ");
            double price = Double.parseDouble(sc.nextLine());
            
            System.out.print("Enter Quantity: ");
            int quantity = Integer.parseInt(sc.nextLine());
            
            System.out.print("Enter Rating (0-5): ");
            double rating = Double.parseDouble(sc.nextLine());
            
            Product product = new Product(id, name, category, price, quantity, rating);
            productManager.addProduct(product);
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid input format! Please enter correct values.");
        } catch (ProductException e) {
            System.out.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Unexpected error: " + e.getMessage());
        } finally {
            System.out.println("Add product operation completed.");
        }
    }
    
    private static void viewAllProducts() {
        System.out.println("\n--- View All Products ---");
        productManager.displayAllProducts();
    }
    
    private static void searchProductById() {
        try {
            System.out.print("\nEnter Product ID to search: ");
            int id = Integer.parseInt(sc.nextLine());
            
            Product product = productManager.searchProductById(id);
            System.out.println("\nProduct Found:");
            System.out.println(product);
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid ID format!");
        } catch (ProductNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    private static void updateProduct() {
        try {
            System.out.println("\n--- Update Product ---");
            System.out.print("Enter Product ID to update: ");
            int id = Integer.parseInt(sc.nextLine());
            
            // Check if product exists
            Product existingProduct = productManager.searchProductById(id);
            System.out.println("Current Product Details: " + existingProduct);
            
            System.out.println("\nEnter new details:");
            
            System.out.print("Enter new Product Name: ");
            String name = sc.nextLine();
            
            System.out.print("Enter new Category: ");
            String category = sc.nextLine();
            
            System.out.print("Enter new Price: ");
            double price = Double.parseDouble(sc.nextLine());
            
            System.out.print("Enter new Quantity: ");
            int quantity = Integer.parseInt(sc.nextLine());
            
            System.out.print("Enter new Rating (0-5): ");
            double rating = Double.parseDouble(sc.nextLine());
            
            Product updatedProduct = new Product(id, name, category, price, quantity, rating);
            productManager.updateProduct(id, updatedProduct);
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid input format!");
        } catch (ProductException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    private static void deleteProduct() {
        try {
            System.out.print("\nEnter Product ID to delete: ");
            int id = Integer.parseInt(sc.nextLine());
            
            productManager.deleteProduct(id);
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid ID format!");
        } catch (ProductNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    private static void searchByCategory() {
        try {
            System.out.print("\nEnter Category to search: ");
            String category = sc.nextLine();
            
            List<Product> products = productManager.searchProductsByCategory(category);
            
            if (products.isEmpty()) {
                System.out.println("No products found in category: " + category);
            } else {
                System.out.println("\nProducts in category '" + category + "':");
                products.forEach(System.out::println);
            }
            
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    private static void filterByPrice() {
        try {
            System.out.print("\nEnter maximum price: ");
            double maxPrice = Double.parseDouble(sc.nextLine());
            
            List<Product> products = productManager.getProductsBelowPrice(maxPrice);
            
            if (products.isEmpty()) {
                System.out.println("No products found below ₹" + maxPrice);
            } else {
                System.out.println("\nProducts below ₹" + maxPrice + ":");
                products.forEach(System.out::println);
            }
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid price format!");
        }
    }
}