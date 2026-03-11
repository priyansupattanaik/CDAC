package com.library.models;

public class Book extends LibraryItem {
	
	private String author;
	private String isbn;
	private String genre;
	private int pageCount;
	private double price;

	public Book() {
		super();
	}

	public Book(int itemID, String title, String publisher, int publicationYear, boolean isAvailable, String author, String isbn, String genre, int pageCount, double price) {
		super(itemID, title, publisher, publicationYear, isAvailable);
		
		this.author = author;
		this.isbn = isbn;
		this.genre = genre;
		this.pageCount = pageCount;
		this.price =price;
		// TODO Auto-generated constructor stub
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getIsbn() {
		return isbn;
	}

	public void setIsbn(String isbn) {
		this.isbn = isbn;
	}

	public String getGenre() {
		return genre;
	}

	public void setGenre(String genre) {
		this.genre = genre;
	}

	public int getPageCount() {
		return pageCount;
	}

	public void setPageCount(int pageCount) {
		this.pageCount = pageCount;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	@Override
	public String getItemType() {
		// TODO Auto-generated method stub
		return "Book";
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + ", Type: Book, Author: " + author + ", Genre: " + genre + ", Price: $" + price + ", Pages: " + pageCount;
	}	
	
}
