package com.university.exceptions;

public class DuplicateCourseCodeException extends RuntimeException {
    public DuplicateCourseCodeException(String message) {
        super(message);
    }
}
