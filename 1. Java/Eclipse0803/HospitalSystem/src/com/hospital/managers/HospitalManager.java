package com.hospital.managers;

import java.util.ArrayList;
import java.util.Comparator;
import com.hospital.models.*;
import com.hospital.exceptions.*;

// This class actually DOES the work
public class HospitalManager extends HospitalOperations {
    
    // ===== DATA STORAGE =====
    // Think of these as filing cabinets
    private ArrayList<Patient> patients;      // Cabinet #1: Patient files
    private ArrayList<Doctor> doctors;        // Cabinet #2: Doctor files
    private ArrayList<Appointment> appointments; // Cabinet #3: Appointment files
    private ArrayList<Ward> wards;            // Cabinet #4: Ward files
    
    // ===== CONSTRUCTOR =====
    public HospitalManager() {
        // Initialize all filing cabinets (empty at first)
        patients = new ArrayList<>();
        doctors = new ArrayList<>();
        appointments = new ArrayList<>();
        wards = new ArrayList<>();
        
        // Add some sample data so we have something to test with
        addSampleData();
    }
    
    // ===== HELPER METHODS (Private - for internal use only) =====
    
    // Helper: Find patient by ID (returns null if not found)
    private Patient findPatientByIdHelper(int id) {
        for (Patient p : patients) {
            if (p.getPersonId() == id) {
                return p;
            }
        }
        return null; // Not found
    }
    
    // Helper: Check if patient ID already exists
    private boolean isDuplicatePatientId(int id) {
        return findPatientByIdHelper(id) != null;
    }
    
    // Helper: Validate patient data
    private void validatePatient(Patient patient) throws InvalidPersonDataException {
        if (patient.getName() == null || patient.getName().trim().isEmpty()) {
            throw new InvalidPersonDataException("Patient name cannot be empty!");
        }
        if (patient.getAge() <= 0 || patient.getAge() > 150) {
            throw new InvalidPersonDataException("Invalid age! Must be between 1 and 150.");
        }
    }
    
    // ===== ADD SAMPLE DATA FOR TESTING =====
    private void addSampleData() {
        try {
            // Add sample patients
            patients.add(new Patient(101, "John Doe", 45, "Male", "Diabetes", true, 201));
            patients.add(new Patient(102, "Jane Smith", 30, "Female", "Flu", false, 202));
            patients.add(new Patient(103, "Bob Johnson", 60, "Male", "Heart Disease", true, 201));
            
            // Add sample doctors
            doctors.add(new Doctor(201, "Dr. Wilson", 50, "Male", "Cardiology", 500.0));
            doctors.add(new Doctor(202, "Dr. Patel", 40, "Female", "General Medicine", 300.0));
            
            // Add sample appointments
            appointments.add(new Appointment(301, 101, 201, "20-03-2024", "10:30", "Scheduled"));
            appointments.add(new Appointment(302, 102, 202, "21-03-2024", "14:00", "Scheduled"));
            
            System.out.println("✅ Sample data loaded successfully!");
        } catch (Exception e) {
            System.out.println("Error loading sample data: " + e.getMessage());
        }
    }
    
    // ===== PATIENT MANAGEMENT METHODS =====
    
    @Override
    public void addPatient(Patient patient) throws DuplicatePatientIdException, InvalidPersonDataException {
        // Step 1: Check if ID already exists
        if (isDuplicatePatientId(patient.getPersonId())) {
            throw new DuplicatePatientIdException("Patient ID " + patient.getPersonId() + " already exists!");
        }
        
        // Step 2: Validate data
        validatePatient(patient);
        
        // Step 3: Add to list
        patients.add(patient);
        System.out.println("✅ Patient added successfully! ID: " + patient.getPersonId());
    }
    
    @Override
    public void viewAllPatients() {
        if (patients.isEmpty()) {
            System.out.println("📭 No patients in the system.");
        } else {
            System.out.println("\n📋 LIST OF ALL PATIENTS (" + patients.size() + "):");
            System.out.println("=".repeat(50));
            
            // Simple for loop for beginners
            for (Patient p : patients) {
                System.out.println(p);
            }
        }
    }
    
    @Override
    public Patient findPatientById(int id) throws PatientNotFoundException {
        Patient patient = findPatientByIdHelper(id);
        if (patient == null) {
            throw new PatientNotFoundException("Patient with ID " + id + " not found!");
        }
        return patient;
    }
    
    @Override
    public void deletePatient(int id) throws PatientNotFoundException {
        Patient patient = findPatientById(id); // This will throw exception if not found
        patients.remove(patient);
        System.out.println("✅ Patient deleted successfully!");
    }
    
    // ===== DOCTOR MANAGEMENT METHODS =====
    
    @Override
    public void addDoctor(Doctor doctor) throws DuplicateDoctorIdException, InvalidPersonDataException {
        // Check duplicate ID
        for (Doctor d : doctors) {
            if (d.getPersonId() == doctor.getPersonId()) {
                throw new DuplicateDoctorIdException("Doctor ID " + doctor.getPersonId() + " already exists!");
            }
        }
        
        // Validate
        if (doctor.getName() == null || doctor.getName().trim().isEmpty()) {
            throw new InvalidPersonDataException("Doctor name cannot be empty!");
        }
        
        doctors.add(doctor);
        System.out.println("✅ Doctor added successfully! ID: " + doctor.getPersonId());
    }
    
    @Override
    public void viewAllDoctors() {
        if (doctors.isEmpty()) {
            System.out.println("📭 No doctors in the system.");
        } else {
            System.out.println("\n📋 LIST OF ALL DOCTORS (" + doctors.size() + "):");
            System.out.println("=".repeat(50));
            for (Doctor d : doctors) {
                System.out.println(d);
            }
        }
    }
    
    @Override
    public Doctor findDoctorById(int id) throws DoctorNotFoundException {
        for (Doctor d : doctors) {
            if (d.getPersonId() == id) {
                return d;
            }
        }
        throw new DoctorNotFoundException("Doctor with ID " + id + " not found!");
    }
    
    // ===== APPOINTMENT MANAGEMENT METHODS =====
    
    @Override
    public void scheduleAppointment(Appointment appointment) throws Exception {
        // Check if patient exists
        try {
            findPatientById(appointment.getPatientId());
        } catch (PatientNotFoundException e) {
            throw new Exception("Cannot schedule: " + e.getMessage());
        }
        
        // Check if doctor exists
        try {
            findDoctorById(appointment.getDoctorId());
        } catch (DoctorNotFoundException e) {
            throw new Exception("Cannot schedule: " + e.getMessage());
        }
        
        // Check duplicate appointment ID
        for (Appointment a : appointments) {
            if (a.getAppointmentId() == appointment.getAppointmentId()) {
                throw new Exception("Appointment ID " + appointment.getAppointmentId() + " already exists!");
            }
        }
        
        appointments.add(appointment);
        System.out.println("✅ Appointment scheduled successfully! ID: " + appointment.getAppointmentId());
    }
    
    // ===== SORTING METHODS (Using Lambda - do this AFTER basic methods work) =====
    
    @Override
    public void sortPatientsByName() {
        System.out.println("\n📋 PATIENTS SORTED BY NAME:");
        System.out.println("=".repeat(50));
        
        // Using lambda to sort
        patients.sort((p1, p2) -> p1.getName().compareTo(p2.getName()));
        
        // Display
        patients.forEach(p -> System.out.println(p));
    }
    
    @Override
    public void sortDoctorsBySpecialization() {
        System.out.println("\n📋 DOCTORS SORTED BY SPECIALIZATION:");
        System.out.println("=".repeat(50));
        
        doctors.sort((d1, d2) -> d1.getSpecialization().compareTo(d2.getSpecialization()));
        doctors.forEach(d -> System.out.println(d));
    }
}