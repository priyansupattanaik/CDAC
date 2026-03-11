package com.cdac.managers;

public abstract class InventoryOperations {

    public abstract void addProduct() throws Exception;

    public abstract void viewProducts();

    public abstract void searchProduct() throws Exception;

    public abstract void updateProduct() throws Exception;

    public abstract void deleteProduct()throws Exception;

    public abstract void sortByName();

    public abstract void sortByCategory();

    public abstract void sortByPrice();

    public abstract void sortByQuantity();

    public abstract void sortByRating();
}