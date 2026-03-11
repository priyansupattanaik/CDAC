package com.inventory.managers;

import com.inventory.exceptions.ProductException;
import com.inventory.models.Product;

public abstract class InventoryOperations {
    
    // Abstract methods
    public abstract void addProduct(Product product) throws ProductException;
    public abstract void updateProduct(int productId, Product updatedProduct) throws ProductException;
    public abstract void deleteProduct(int productId) throws ProductException;
    public abstract Product searchProductById(int productId) throws ProductException;
    public abstract void displayAllProducts();
    
    // Concrete method - common for all inventory operations
    public void displayWelcomeMessage() {
        System.out.println("Welcome to Inventory Management System");
    }
    
    // Validation method
    protected boolean validateProduct(Product product) throws InvalidProductDataException {
        if (product == null) {
            throw new InvalidProductDataException("Product cannot be null");
        }
        if (product.getProductId() <= 0) {
            throw new InvalidProductDataException("Product ID must be positive");
        }
        if (product.getProductName() == null || product.getProductName().trim().isEmpty()) {
            throw new InvalidProductDataException("Product name cannot be empty");
        }
        if (product.getPrice() <= 0) {
            throw new InvalidProductDataException("Price must be greater than 0");
        }
        if (product.getQuantity() < 0) {
            throw new InvalidProductDataException("Quantity cannot be negative");
        }
        if (product.getRating() < 0 || product.getRating() > 5) {
            throw new InvalidProductDataException("Rating must be between 0 and 5");
        }
        return true;
    }
}