package com.cdac.models;

public class Patient {
	
	private int PatientId;
	private String Name;
	private String Disease;
	private String BloodGroup;
	private int WardNo;
	private int Age;
	private String DoctorName;
	
	
	
	
	public int getPatientId() {
		return PatientId;
	}

	public void setPatientId(int patientId) {
		PatientId = patientId;
	}

	public String getName() {
		return Name;
	}

	public void setName(String name) {
		Name = name;
	}

	public String getDisease() {
		return Disease;
	}

	public void setDisease(String disease) {
		Disease = disease;
	}

	public String getBloodGroup() {
		return BloodGroup;
	}

	public void setBloodGroup(String bloodGroup) {
		BloodGroup = bloodGroup;
	}

	public int getWardNo() {
		return WardNo;
	}

	public void setWardNo(int wardNo) {
		WardNo = wardNo;
	}

	public int getAge() {
		return Age;
	}

	public void setAge(int age) {
		Age = age;
	}

	public String getDoctorName() {
		return DoctorName;
	}

	public void setDoctorName(String doctorName) {
		DoctorName = doctorName;
	}

	public Patient() {
		super();
	}

	public Patient(int patientId, String name, String disease, String bloodGroup, int wardNo, int age,
			String doctorName) {
		super();
		PatientId = patientId;
		Name = name;
		Disease = disease;
		BloodGroup = bloodGroup;
		WardNo = wardNo;
		Age = age;
		DoctorName = doctorName;
	}

	@Override
	public String toString() {
		return "PatientId=" + PatientId + ", Name=" + Name + ", Disease=" + Disease + ", BloodGroup="
				+ BloodGroup + ", WardNo=" + WardNo + ", Age=" + Age + ", DoctorName=" + DoctorName;
	}
	
	
}
