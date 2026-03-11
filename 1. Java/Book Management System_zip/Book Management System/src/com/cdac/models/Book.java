package com.cdac.models;

public class Book {

    private int bookId;
    private String title;
    private String author;
    private double price;
    private double rating;
    private int publicationYear;

    public Book() {}

    public Book(int bookId, String title, String author, double price, double rating, int publicationYear) {
        this.bookId = bookId;
        this.title = title;
        this.author = author;
        this.price = price;
        this.rating = rating;
        this.publicationYear = publicationYear;
    }

    public int getBookId() {
        return bookId;
    }

    public void setBookId(int bookId) {
        this.bookId = bookId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    public int getPublicationYear() {
        return publicationYear;
    }

    public void setPublicationYear(int publicationYear) {
        this.publicationYear = publicationYear;
    }

    @Override
    public String toString() {
        return "Book ID: " + bookId +
                "\nTitle: " + title +
                "\nAuthor: " + author +
                "\nPrice: " + price +
                "\nRating: " + rating +
                "\nPublication Year: " + publicationYear +
                "\n---------------------------";
    }
}