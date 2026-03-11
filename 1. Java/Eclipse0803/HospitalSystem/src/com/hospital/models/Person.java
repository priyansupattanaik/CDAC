package com.hospital.models;

public abstract class Person {
	
	private int personID;
	private String name;
	private int age;
	private String gender;
	public Person(int personID, String name, int age, String gender) {
		super();
		this.personID = personID;
		this.name = name;
		this.age = age;
		this.gender = gender;
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
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	
	public abstract String getRole();
	@Override
	public String toString() {
		return "Person [personID=" + personID + ", name=" + name + ", age=" + age + ", gender=" + gender + "]";
	}
	
	
	

}
