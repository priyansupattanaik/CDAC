package com.cdac.managers;

import com.cdac.models.Product;
import com.cdac.exceptions.*;

import java.util.*;

public class ProductManager extends InventoryOperations {

     ArrayList<Product> products = new ArrayList<>();
     
     public ProductManager() {
    	 products.add(new Product(1, "ABC", "XY", 150.00, 100, 9.8));
    	 products.add(new Product(3, "XYZ", "AB", 50.99, 10, 7.1));
    	 products.add(new Product(5, "MNO", "RS", 183.53, 550, 8.3));
    	 products.add(new Product(4, "DAI", "PQ", 100.42, 631, 5.5));
    	 products.add(new Product(2, "ZEB", "CD", 199.99, 114, 1.2));
     }
     Scanner sc = new Scanner(System.in);

    @Override
    public void addProduct() throws DuplicateProductIdException, InvalidProductDataException {

        try {

            System.out.print("Enter Product ID: ");
            int id = sc.nextInt();
            sc.nextLine();

            for (Product p : products) {
                if (p.getProductId() == id) {
                    throw new DuplicateProductIdException("Product ID already exists!");
                }
            }

            System.out.print("Enter Product Name: ");
            String name = sc.nextLine();

            System.out.print("Enter Category: ");
            String category = sc.nextLine();

            System.out.print("Enter Price: ");
            double price = sc.nextDouble();

            System.out.print("Enter Quantity: ");
            int quantity = sc.nextInt();

            System.out.print("Enter Rating: ");
            double rating = sc.nextDouble();

            if (price < 0 || quantity < 0) {
                throw new InvalidProductDataException("Price or Quantity cannot be negative.");
            }

            Product p = new Product();

            p.setProductId(id);
            p.setProductName(name);
            p.setCategory(category);
            p.setPrice(price);
            p.setQuantity(quantity);
            p.setRating(rating);

            products.add(p);

            System.out.println("Product added successfully.");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public void viewProducts() {

        if (products.isEmpty()) {
            System.out.println("No products available.");
            return;
        }

        for (Product p : products) {
            System.out.println(p);
        }
    }

    @Override
    public void searchProduct() throws ProductNotFoundException {

        try {

            System.out.print("Enter Product ID to search: ");
            int id = sc.nextInt();

            for (Product p : products) {
                if (p.getProductId() == id) {
                    System.out.println(p);
                    return;
                }
            }

            throw new ProductNotFoundException("Product not found!");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public void updateProduct() throws ProductNotFoundException {

        try {

            System.out.print("Enter Product ID to update: ");
            int id = sc.nextInt();
            sc.nextLine();

            for (Product p : products) {

                if (p.getProductId() == id) {

                    System.out.print("Enter New Name: ");
                    p.setProductName(sc.nextLine());

                    System.out.print("Enter New Category: ");
                    p.setCategory(sc.nextLine());

                    System.out.print("Enter New Price: ");
                    p.setPrice(sc.nextDouble());

                    System.out.print("Enter New Quantity: ");
                    p.setQuantity(sc.nextInt());

                    System.out.print("Enter New Rating: ");
                    p.setRating(sc.nextDouble());

                    System.out.println("Product updated successfully.");
                    return;
                }
            }

            throw new ProductNotFoundException("Product not found!");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    @Override
    public void deleteProduct() throws ProductNotFoundException {

        try {

            System.out.print("Enter Product ID to delete: ");
            int id = sc.nextInt();
 
            Product removeProduct = null;

            for (Product p : products) {
                if (p.getProductId() == id) {
                    removeProduct = p;
                    break;
                }
            }

            if (removeProduct == null) {
                throw new ProductNotFoundException("Product not found!");
            }

            products.remove(removeProduct);

            System.out.println("Product deleted successfully.");

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    
//    public void deleteProduct() {
//
//        try {
//
//            System.out.print("Enter Product ID to delete: ");
//            int id = sc.nextInt();
//
//            boolean removed = products.removeIf(p -> p.getProductId() == id);
//
//            if (!removed) {
//                throw new ProductNotFoundException("Product not found!");
//            }
//
//            System.out.println("Product deleted successfully.");
//
//        } catch (ProductNotFoundException e) {
//            System.out.println(e.getMessage());
//        } catch (Exception e) {
//            System.out.println("Invalid input!");
//        } finally {
//            System.out.println("Delete operation completed.");
//        }
//    }

    @Override
    public void sortByName() {

        Collections.sort(products, (p1, p2) -> p1.getProductName().compareToIgnoreCase(p2.getProductName()));

        viewProducts();
    }

    @Override
    public void sortByCategory() {

        Collections.sort(products, (p1, p2) -> p1.getCategory().compareToIgnoreCase(p2.getCategory()));

        viewProducts();
    }

    @Override
    public void sortByPrice() {

        Collections.sort(products, (p1, p2) -> Double.compare(p1.getPrice(), p2.getPrice()));
        viewProducts();
    }

    @Override
    public void sortByQuantity() {

        Collections.sort(products, (p1, p2) -> Integer.compare(p1.getQuantity(), p2.getQuantity()));

        viewProducts();
    }

    @Override
    public void sortByRating() {

        Collections.sort(products, (p1, p2) -> Double.compare(p2.getRating(), p1.getRating()));

        viewProducts();
    }
}
