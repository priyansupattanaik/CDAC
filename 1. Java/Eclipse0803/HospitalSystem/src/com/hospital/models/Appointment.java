package com.hospital.models;

public class Appointment {
    private int appointmentId;   // Unique appointment number
    private int patientId;        // Which patient?
    private int doctorId;         // Which doctor?
    private String date;          // When? (DD-MM-YYYY)
    private String time;          // What time? (HH:MM)
    private String status;        // Scheduled, Completed, Cancelled
    
    public Appointment(int appointmentId, int patientId, int doctorId, 
                       String date, String time, String status) {
        this.appointmentId = appointmentId;
        this.patientId = patientId;
        this.doctorId = doctorId;
        this.date = date;
        this.time = time;
        this.status = status;
    }
    
    // Getters and Setters
    public int getAppointmentId() { return appointmentId; }
    public void setAppointmentId(int appointmentId) { this.appointmentId = appointmentId; }
    
    public int getPatientId() { return patientId; }
    public void setPatientId(int patientId) { this.patientId = patientId; }
    
    public int getDoctorId() { return doctorId; }
    public void setDoctorId(int doctorId) { this.doctorId = doctorId; }
    
    public String getDate() { return date; }
    public void setDate(String date) { this.date = date; }
    
    public String getTime() { return time; }
    public void setTime(String time) { this.time = time; }
    
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
    
    @Override
    public String toString() {
        return "Appointment #" + appointmentId + ": Patient " + patientId + 
               " with Doctor " + doctorId + " on " + date + " at " + time + 
               " [" + status + "]";
    }
}