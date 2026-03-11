package com.university.models;
import java.util.ArrayList;

public class Student extends Person {
	
	private int studentID;
	private int enrollmentYear;
	private int semester;
	private double cgpa;
	private String major;
	private int creditsCompleted;
	private boolean isActive;
	private double scholarshipAmount;
	private ArrayList<String> enrolledCourses;
	
	public Student(int personID, String name, String email, String phoneNumber, String address,
			int studentID, int enrollmentYear, int semester, double cgpa, String major,
			int creditsCompleted, boolean isActive, double scholarshipAmount) {
		super(personID, name, email, phoneNumber, address);
		this.studentID = studentID;
		this.enrollmentYear = enrollmentYear;
		this.semester = semester;
		this.cgpa = cgpa;
		this.major = major;
		this.creditsCompleted = creditsCompleted;
		this.isActive = isActive;
		this.scholarshipAmount = scholarshipAmount;
		this.enrolledCourses = new ArrayList<>();
	}
	
	public int getStudentID() {
		return studentID;
	}
	
	public void setStudentID(int studentID) {
		this.studentID = studentID;
	}
	
	public int getEnrollmentYear() {
		return enrollmentYear;
	}
	
	public void setEnrollmentYear(int enrollmentYear) {
		this.enrollmentYear = enrollmentYear;
	}
	
	public int getSemester() {
		return semester;
	}
	
	public void setSemester(int semester) {
		this.semester = semester;
	}
	
	public double getCgpa() {
		return cgpa;
	}
	
	public void setCgpa(double cgpa) {
		this.cgpa = cgpa;
	}
	
	public String getMajor() {
		return major;
	}
	
	public void setMajor(String major) {
		this.major = major;
	}
	
	public int getCreditsCompleted() {
		return creditsCompleted;
	}
	
	public void setCreditsCompleted(int creditsCompleted) {
		this.creditsCompleted = creditsCompleted;
	}
	
	public boolean isActive() {
		return isActive;
	}
	
	public void setActive(boolean isActive) {
		this.isActive = isActive;
	}
	
	public double getScholarshipAmount() {
		return scholarshipAmount;
	}
	
	public void setScholarshipAmount(double scholarshipAmount) {
		this.scholarshipAmount = scholarshipAmount;
	}
	
	public ArrayList<String> getEnrolledCourses() {
		return enrolledCourses;
	}
	
	public void addEnrollCourse(String courseCode) {
		this.enrolledCourses.add(courseCode);
	}
	
	@Override
	public String getRole() {
		return "Student";
	}
	
	@Override
	public String getDepartment() {
		return major;
	}

}
