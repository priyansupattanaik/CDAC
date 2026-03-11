package com.cdac.managers;

public abstract class LibraryOperations {

    public abstract void addBook() throws Exception;

    public abstract void viewBooks();

    public abstract void searchBook() throws Exception;

    public abstract void updateBook() throws Exception;

    public abstract void deleteBook() throws Exception;

    public abstract void sortByTitle();

    public abstract void sortByAuthor();

    public abstract void sortByPrice();

    public abstract void sortByRating();

    public abstract void sortByPublicationYear();
}