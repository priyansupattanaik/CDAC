package com.university.exceptions;

public class MaxCreditsExceededException extends RuntimeException {
    public MaxCreditsExceededException(String message) {
        super(message);
    }
}
