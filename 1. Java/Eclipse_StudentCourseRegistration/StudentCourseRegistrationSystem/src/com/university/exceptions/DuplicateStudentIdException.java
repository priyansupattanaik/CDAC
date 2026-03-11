package com.university.exceptions;

public class DuplicateStudentIdException extends RuntimeException {
    public DuplicateStudentIdException(String message) {
        super(message);
    }
}
