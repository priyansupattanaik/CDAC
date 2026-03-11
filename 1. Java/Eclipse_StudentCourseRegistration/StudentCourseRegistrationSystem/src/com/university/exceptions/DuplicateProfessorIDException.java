package com.university.exceptions;

public class DuplicateProfessorIdException extends RuntimeException {
    public DuplicateProfessorIdException(String message) {
        super(message);
    }
}
