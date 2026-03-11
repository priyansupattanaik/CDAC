package com.hospital.models;

import java.util.ArrayList;

public class Doctor extends Person {
    private String specialization;  // Heart doctor? Brain doctor?
    private double consultationFee; // How much they charge
    private ArrayList<String> availableDays; // When they work
    
    public Doctor(int personId, String name, int age, String gender,
                  String specialization, double consultationFee) {
        super(personId, name, age, gender);
        this.specialization = specialization;
        this.consultationFee = consultationFee;
        this.availableDays = new ArrayList<>();
    }
    
    public String getSpecialization() { return specialization; }
    public void setSpecialization(String specialization) { this.specialization = specialization; }
    
    public double getConsultationFee() { return consultationFee; }
    public void setConsultationFee(double consultationFee) { this.consultationFee = consultationFee; }
    
    public ArrayList<String> getAvailableDays() { return availableDays; }
    public void setAvailableDays(ArrayList<String> availableDays) { this.availableDays = availableDays; }
    
    // Helper method to add a day
    public void addAvailableDay(String day) {
        availableDays.add(day);
    }
    
    @Override
    public String getRole() {
        return "Doctor";
    }
    
    @Override
    public String toString() {
        return super.toString() + ", Specialization: " + specialization + 
               ", Fee: $" + consultationFee;
    }
}