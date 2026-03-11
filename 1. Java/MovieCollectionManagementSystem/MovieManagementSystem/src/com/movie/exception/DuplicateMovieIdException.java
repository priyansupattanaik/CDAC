package com.movie.exception;

public class DuplicateMovieIdException extends Exception {

    public DuplicateMovieIdException(String message) {
        super(message);
    }
}