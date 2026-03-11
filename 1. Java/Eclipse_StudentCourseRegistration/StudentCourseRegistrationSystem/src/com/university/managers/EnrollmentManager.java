package com.university.managers;

import com.university.models.Enrollment;
import com.university.exceptions.EnrollmentNotFoundException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;

public class EnrollmentManager extends AbstractManager<Enrollment> {
    private int nextEnrollmentId = 4001;
    
    public EnrollmentManager() {
        this.records = new ArrayList<>();
    }
    
    @Override
    public void add(Enrollment enrollment) {
        enrollment.setEnrollmentId(nextEnrollmentId++);
        records.add(enrollment);
    }

    @Override
    public Enrollment findById(int id) {
        return records.stream()
                .filter(e -> e.getEnrollmentId() == id)
                .findFirst()
                .orElse(null);
    }

    @Override
    public void update(Enrollment enrollment) {
        Enrollment existing = findById(enrollment.getEnrollmentId());
        if (existing == null) {
            throw new EnrollmentNotFoundException("Enrollment with ID " + enrollment.getEnrollmentId() + " not found");
        }
        records.remove(existing);
        records.add(enrollment);
    }

    @Override
    public void delete(int id) {
        Enrollment enrollment = findById(id);
        if (enrollment == null) {
            throw new EnrollmentNotFoundException("Enrollment with ID " + id + " not found");
        }
        records.remove(enrollment);
    }

    @Override
    public List<Enrollment> getAll() {
        return records;
    }
    
    // Stream API usage for searching
    public List<Enrollment> getEnrollmentsByStudentId(int studentId) {
        return records.stream()
                .filter(e -> e.getStudentId() == studentId)
                .toList();
    }
    
    public List<Enrollment> getEnrollmentsByCourseCode(String courseCode) {
        return records.stream()
                .filter(e -> e.getCourseCode().equalsIgnoreCase(courseCode))
                .toList();
    }
    
    // Sorting by enrollment date
    public List<Enrollment> getEnrollmentsSortedByDate() {
        return records.stream()
                .sorted(Comparator.comparing(Enrollment::getEnrollmentDate))
                .toList();
    }
}
