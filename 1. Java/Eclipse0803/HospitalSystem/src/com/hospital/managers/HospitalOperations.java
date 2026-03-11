package com.hospital.managers;

import com.hospital.models.*;
import com.hospital.exceptions.*;

public abstract class HospitalOperations {
	
	public abstract void addPatient(Patient patient) throws DuplicatePatientIDException, InvalidPersonDataException;
	public abstract void viewAllPatients();
	public abstract void findPatientByID(int ID) throws PatientNotFoundException;
	public abstract void deletePatientByID(int ID) throws PatientNotFoundException;
	
	public abstract void addDoctor(Doctor doctor) throws DuplicateDoctorIDException, InvalidPersonDataException;
	public abstract void viewAllDoctors();
	public abstract void findDoctorByID(int ID) throws DoctorNotFoundException;
	
	public abstract void scheduleAppointment(Appointment appointment) throws Exception;
	
	public abstract void sortPatientsByName();
	public abstract void sortDoctorsBySpecialization();

}
