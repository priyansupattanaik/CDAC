package com.hospital.exceptions;

public class DuplicatePatientIDException extends Exception {
	
	public DuplicatePatientIDException(String Message) {
		super(Message);
	}

}
