package com.university.models;

import java.util.ArrayList;

public class Course {
	
	private String courseCode;
	private String courseName;
	private int credits;
	private String department;
	private int professorID;
	private int semesterOffered;
	private int maxSeats;
	private int enrolledCount;
	private boolean isAvailable;
	private ArrayList<String> prerequisites;
	private String schedule;
	
	public Course(String courseCode, String courseName, int credits, String department,
			int professorID, int semesterOffered, int maxSeats, String schedule) {
		this.courseCode = courseCode;
		this.courseName = courseName;
		this.credits = credits;
		this.department = department;
		this.professorID = professorID;
		this.semesterOffered = semesterOffered;
		this.maxSeats = maxSeats;
		this.enrolledCount = 0;
		this.isAvailable = true;
		this.prerequisites = new ArrayList<>();
		this.schedule = schedule;
	}
	
	public String getCourseCode() {
		return courseCode;
	}
	
	public void setCourseCode(String courseCode) {
		this.courseCode = courseCode;
	}
	
	public String getCourseName() {
		return courseName;
	}
	
	public void setCourseName(String courseName) {
		this.courseName = courseName;
	}
	
	public int getCredits() {
		return credits;
	}
	
	public void setCredits(int credits) {
		this.credits = credits;
	}
	
	public String getDepartment() {
		return department;
	}
	
	public void setDepartment(String department) {
		this.department = department;
	}
	
	public int getProfessorID() {
		return professorID;
	}
	
	public void setProfessorID(int professorID) {
		this.professorID = professorID;
	}
	
	public int getSemesterOffered() {
		return semesterOffered;
	}
	
	public void setSemesterOffered(int semesterOffered) {
		this.semesterOffered = semesterOffered;
	}
	
	public int getMaxSeats() {
		return maxSeats;
	}
	
	public void setMaxSeats(int maxSeats) {
		this.maxSeats = maxSeats;
	}
	
	public int getEnrolledCount() {
		return enrolledCount;
	}
	
	public void setEnrolledCount(int enrolledCount) {
		this.enrolledCount = enrolledCount;
	}
	
	public boolean isAvailable() {
		return isAvailable;
	}
	
	public void setAvailable(boolean isAvailable) {
		this.isAvailable = isAvailable;
	}
	
	public ArrayList<String> getPrerequisites() {
		return prerequisites;
	}
	
	public void addPrerequisite(String courseCode) {
		this.prerequisites.add(courseCode);
	}
	
	public String getSchedule() {
		return schedule;
	}
	
	public void setSchedule(String schedule) {
		this.schedule = schedule;
	}
	
	public boolean enrollStudent() {
		if (enrolledCount < maxSeats) {
			enrolledCount++;
			return true;
		}
		return false;
	}
	
	public void dropStudent() {
		if (enrolledCount > 0) {
			enrolledCount--;
		}
		if (enrolledCount == 0) {
			isAvailable = true;
		}
	}

}
