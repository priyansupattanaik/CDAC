package com.university.models;

public abstract class Person {
	
	private int personID;
	private String name;
	private String email;
	private String phoneNumber;
	private String address;
	
	public Person(int personID, String name, String email, String phoneNumber, String address) {
		this.personID = personID;
		this.name = name;
		this.email = email;
		this.phoneNumber = phoneNumber;
		this.address = address;
	}
	
	public int getPersonID() {
		return personID;
	}
	
	public void setPersonID(int personID) {
		this.personID = personID;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public String getEmail() {
		return email;
	}
	
	public void setEmail(String email) {
		this.email = email;
	}
	
	public String getPhoneNumber() {
		return phoneNumber;
	}
	
	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}
	
	public String getAddress() {
		return address;
	}
	
	public void setAddress(String address) {
		this.address = address;
	}
	
	public abstract String getRole();
	
	public abstract String getDepartment();

}
