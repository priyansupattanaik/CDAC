package com.inventory.models;

public class Product {
    
    // Private attributes - Encapsulation
    private int productId;
    private String productName;
    private String category;
    private double price;
    private int quantity;
    private double rating;
    
    // Default Constructor
    public Product() {
        super();
    }
    
    // Parameterized Constructor
    public Product(int productId, String productName, String category, 
                   double price, int quantity, double rating) {
        super();
        this.productId = productId;
        this.productName = productName;
        this.category = category;
        this.price = price;
        this.quantity = quantity;
        this.rating = rating;
    }
    
    // Getters and Setters
    public int getProductId() {
        return productId;
    }
    
    public void setProductId(int productId) {
        this.productId = productId;
    }
    
    public String getProductName() {
        return productName;
    }
    
    public void setProductName(String productName) {
        this.productName = productName;
    }
    
    public String getCategory() {
        return category;
    }
    
    public void setCategory(String category) {
        this.category = category;
    }
    
    public double getPrice() {
        return price;
    }
    
    public void setPrice(double price) {
        this.price = price;
    }
    
    public int getQuantity() {
        return quantity;
    }
    
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    
    public double getRating() {
        return rating;
    }
    
    public void setRating(double rating) {
        this.rating = rating;
    }
    
    // Override toString method
    @Override
    public String toString() {
        return String.format("Product ID: %d | Name: %-15s | Category: %-12s | Price: ₹%.2f | Quantity: %d | Rating: %.1f",
                productId, productName, category, price, quantity, rating);
    }
}