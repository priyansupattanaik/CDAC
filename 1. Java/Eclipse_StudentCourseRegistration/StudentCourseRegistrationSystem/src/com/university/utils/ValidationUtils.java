package com.university.utils;

public class ValidationUtils {
    public static boolean isValidEmail(String email) {
        if (email == null || email.isEmpty()) return false;
        return email.matches("^[A-Za-z0-9+_.-]+@(.+)$");
    }
    
    public static boolean isValidPhone(String phone) {
        if (phone == null || phone.isEmpty()) return false;
        return phone.matches("^[0-9]{10}$");
    }
    
    public static boolean isValidGrade(String grade) {
        if (grade == null || grade.isEmpty()) return false;
        return grade.matches("^[A-D][+-]?$");
    }
}
