package com.library.models;

public abstract class LibraryItem {
	
	private int itemID;
	private String title;
	private String publisher;
	private int publicationYear;
	private boolean isAvailable;
	
	public LibraryItem() {}
	
	public LibraryItem(int itemID, String title, String publisher, int publicationYear, boolean isAvailable) {
		this.itemID = itemID;
		this.title = title;
		this.publisher = publisher;
		this.publicationYear = publicationYear;
		this.isAvailable = isAvailable;
	}

	public int getItemID() {
		return itemID;
	}

	public void setItemID(int itemID) {
		this.itemID = itemID;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getPublisher() {
		return publisher;
	}

	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}

	public int getPublicationYear() {
		return publicationYear;
	}

	public void setPublicationYear(int publicationYear) {
		this.publicationYear = publicationYear;
	}

	public boolean isAvailable() {
		return isAvailable;
	}

	public void setAvailable(boolean isAvailable) {
		this.isAvailable = isAvailable;
	}
	
	public abstract String getItemType();
	
	@Override
	public String toString() {
		return "ID:" + itemID + ", Title:" + title + ", Publisher:" + publisher + ", Year="
				+ publicationYear + ", Available: " + (isAvailable ? "Yes" : "No");
	}
	

}
