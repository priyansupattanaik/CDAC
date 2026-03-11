package com.cdac.exceptions;

public class DuplicateBookIdException extends Exception {

    public DuplicateBookIdException(String message) {
        super(message);
    }
}