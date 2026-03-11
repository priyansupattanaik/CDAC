package com.library.models;

public class Magazine extends LibraryItem {
	
	private int issueNumber;
	private String frequency;
	private String editor;
	
	public Magazine() {
		super();
	}

	public Magazine(int itemID, String title, String publisher, int publicationYear, boolean isAvailable, int issueNumber, String frequency, String editor) {
		super(itemID, title, publisher, publicationYear, isAvailable);
		
		this.issueNumber =issueNumber;
		this.frequency =frequency;
		this.editor = editor;
		
		
		// TODO Auto-generated constructor stub
	}

	public int getIssueNumber() {
		return issueNumber;
	}

	public void setIssueNumber(int issueNumber) {
		this.issueNumber = issueNumber;
	}

	public String getFrequency() {
		return frequency;
	}

	public void setFrequency(String frequency) {
		this.frequency = frequency;
	}

	public String getEditor() {
		return editor;
	}

	public void setEditor(String editor) {
		this.editor = editor;
	}

	@Override
	public String getItemType() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString() + ",Type: Magazine, Issue: " + issueNumber + ", Frequency: " + frequency + ", Editor: " + editor;
	}

}
