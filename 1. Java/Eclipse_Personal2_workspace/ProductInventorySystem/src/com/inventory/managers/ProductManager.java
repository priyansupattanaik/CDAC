package com.inventory.managers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

import com.inventory.exceptions.*;
import com.inventory.models.Product;

public class ProductManager extends InventoryOperations {
    
    private ArrayList<Product> productList;
    
    public ProductManager() {
        productList = new ArrayList<>();
        // Add some sample data
        initializeSampleData();
    }
    
    private void initializeSampleData() {
        try {
            productList.add(new Product(101, "Laptop", "Electronics", 55000.00, 10, 4.5));
            productList.add(new Product(102, "Mouse", "Electronics", 500.00, 50, 4.0));
            productList.add(new Product(103, "Desk", "Furniture", 8000.00, 15, 3.5));
            productList.add(new Product(104, "Notebook", "Stationery", 50.00, 200, 4.8));
            productList.add(new Product(105, "Printer", "Electronics", 12000.00, 8, 4.2));
        } catch (Exception e) {
            System.out.println("Error initializing sample data: " + e.getMessage());
        }
    }
    
    @Override
    public void addProduct(Product product) throws ProductException {
        // Validate product data
        validateProduct(product);
        
        // Check for duplicate ID
        boolean idExists = productList.stream()
                .anyMatch(p -> p.getProductId() == product.getProductId());
        
        if (idExists) {
            throw new DuplicateProductIdException(
                "Product with ID " + product.getProductId() + " already exists!");
        }
        
        // Add product
        productList.add(product);
        System.out.println("Product added successfully!");
    }
    
    @Override
    public void updateProduct(int productId, Product updatedProduct) throws ProductException {
        // Validate updated product data
        validateProduct(updatedProduct);
        
        // Find and update product
        boolean found = false;
        for (int i = 0; i < productList.size(); i++) {
            if (productList.get(i).getProductId() == productId) {
                productList.set(i, updatedProduct);
                found = true;
                System.out.println("Product updated successfully!");
                break;
            }
        }
        
        if (!found) {
            throw new ProductNotFoundException("Product with ID " + productId + " not found!");
        }
    }
    
    @Override
    public void deleteProduct(int productId) throws ProductException {
        boolean removed = productList.removeIf(p -> p.getProductId() == productId);
        
        if (!removed) {
            throw new ProductNotFoundException("Product with ID " + productId + " not found!");
        }
        
        System.out.println("Product deleted successfully!");
    }
    
    @Override
    public Product searchProductById(int productId) throws ProductException {
        return productList.stream()
                .filter(p -> p.getProductId() == productId)
                .findFirst()
                .orElseThrow(() -> new ProductNotFoundException(
                    "Product with ID " + productId + " not found!"));
    }
    
    @Override
    public void displayAllProducts() {
        if (productList.isEmpty()) {
            System.out.println("No products in inventory!");
            return;
        }
        
        System.out.println("\n" + "=".repeat(100));
        System.out.println("PRODUCT INVENTORY");
        System.out.println("=".repeat(100));
        
        productList.stream()
                .forEach(System.out::println);
        
        System.out.println("=".repeat(100));
        System.out.println("Total Products: " + productList.size());
    }
    
    // Sorting methods using Lambda Expressions (Functional Interface)
    
    public void sortProductsByName() {
        Collections.sort(productList, 
            (p1, p2) -> p1.getProductName().compareToIgnoreCase(p2.getProductName()));
        System.out.println("\nProducts sorted by name:");
        displayAllProducts();
    }
    
    public void sortProductsByCategory() {
        productList.sort(Comparator.comparing(Product::getCategory));
        System.out.println("\nProducts sorted by category:");
        displayAllProducts();
    }
    
    public void sortProductsByPrice() {
        productList.sort((p1, p2) -> Double.compare(p1.getPrice(), p2.getPrice()));
        System.out.println("\nProducts sorted by price (low to high):");
        displayAllProducts();
    }
    
    public void sortProductsByPriceDescending() {
        productList.sort((p1, p2) -> Double.compare(p2.getPrice(), p1.getPrice()));
        System.out.println("\nProducts sorted by price (high to low):");
        displayAllProducts();
    }
    
    public void sortProductsByQuantity() {
        productList.sort(Comparator.comparingInt(Product::getQuantity));
        System.out.println("\nProducts sorted by quantity:");
        displayAllProducts();
    }
    
    public void sortProductsByRating() {
        productList.sort((p1, p2) -> Double.compare(p2.getRating(), p1.getRating()));
        System.out.println("\nProducts sorted by rating (highest first):");
        displayAllProducts();
    }
    
    // Additional search methods
    public List<Product> searchProductsByCategory(String category) {
        return productList.stream()
                .filter(p -> p.getCategory().equalsIgnoreCase(category))
                .collect(Collectors.toList());
    }
    
    public List<Product> getProductsBelowPrice(double maxPrice) {
        return productList.stream()
                .filter(p -> p.getPrice() <= maxPrice)
                .collect(Collectors.toList());
    }
    
    public void updateQuantity(int productId, int newQuantity) throws ProductException {
        Product product = searchProductById(productId);
        if (newQuantity < 0) {
            throw new InvalidProductDataException("Quantity cannot be negative!");
        }
        product.setQuantity(newQuantity);
        System.out.println("Quantity updated successfully!");
    }
}