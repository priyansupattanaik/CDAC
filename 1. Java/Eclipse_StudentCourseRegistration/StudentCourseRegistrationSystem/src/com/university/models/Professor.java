package com.university.models;

import java.util.ArrayList;

public class Professor extends Person {
    private int professorId;
    private String department;
    private String designation;
    private String qualification;
    private int experienceYears;
    private String specialization;
    private ArrayList<String> coursesTaught;
    private double salary;

    public Professor(int personId, int professorId, String name, String email, String phone, String address,
                     String department, String designation, String qualification, int experienceYears,
                     String specialization, double salary) {
        super(personId, name, email, phone, address);
        this.professorId = professorId;
        this.department = department;
        this.designation = designation;
        this.qualification = qualification;
        this.experienceYears = experienceYears;
        this.specialization = specialization;
        this.coursesTaught = new ArrayList<>();
        this.salary = salary;
    }

    public int getProfessorId() {
        return professorId;
    }

    public void setProfessorId(int professorId) {
        this.professorId = professorId;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getDesignation() {
        return designation;
    }

    public void setDesignation(String designation) {
        this.designation = designation;
    }

    public String getQualification() {
        return qualification;
    }

    public void setQualification(String qualification) {
        this.qualification = qualification;
    }

    public int getExperienceYears() {
        return experienceYears;
    }

    public void setExperienceYears(int experienceYears) {
        this.experienceYears = experienceYears;
    }

    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }

    public ArrayList<String> getCoursesTaught() {
        return coursesTaught;
    }

    public void addCourseTaught(String courseCode) {
        this.coursesTaught.add(courseCode);
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    @Override
    public String getRole() {
        return "Professor";
    }

    @Override
    public String getDepartment() {
        return this.department;
    }
}
