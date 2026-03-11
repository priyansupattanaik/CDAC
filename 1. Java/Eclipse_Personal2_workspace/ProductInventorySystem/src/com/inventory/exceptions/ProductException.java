package com.inventory.exceptions;

public class ProductException extends Exception {
    public ProductException(String message) {
        super(message);
    }
}

// Specific exception classes
class ProductNotFoundException extends ProductException {
    public ProductNotFoundException(String message) {
        super(message);
    }
}

class DuplicateProductIdException extends ProductException {
    public DuplicateProductIdException(String message) {
        super(message);
    }
}

class InvalidProductDataException extends ProductException {
    public InvalidProductDataException(String message) {
        super(message);
    }
}