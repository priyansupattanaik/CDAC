package com.university.managers;

import com.university.models.Student;
import com.university.exceptions.StudentNotFoundException;
import com.university.exceptions.DuplicateStudentIdException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;

public class StudentManager extends AbstractManager<Student> {
    private int nextStudentId = 1001;
    
    public StudentManager() {
        this.records = new ArrayList<>();
    }
    
    @Override
    public void add(Student student) {
        if (findById(student.getStudentID()) != null) {
            throw new DuplicateStudentIdException("Student with ID " + student.getStudentID() + " already exists");
        }
        student.setPersonID(nextStudentId++);
        records.add(student);
    }

    @Override
    public Student findById(int id) {
        return records.stream()
                .filter(s -> s.getStudentID() == id)
                .findFirst()
                .orElse(null);
    }

    @Override
    public void update(Student student) {
        Student existing = findById(student.getStudentID());
        if (existing == null) {
            throw new StudentNotFoundException("Student with ID " + student.getStudentID() + " not found");
        }
        records.remove(existing);
        records.add(student);
    }

    @Override
    public void delete(int id) {
        Student student = findById(id);
        if (student == null) {
            throw new StudentNotFoundException("Student with ID " + id + " not found");
        }
        records.remove(student);
    }

    @Override
    public List<Student> getAll() {
        return records;
    }
    
    // Stream API usage for searching
    public List<Student> searchStudentsByName(String name) {
        return records.stream()
                .filter(s -> s.getName().toLowerCase().contains(name.toLowerCase()))
                .toList();
    }
    
    public List<Student> getStudentsByMajor(String major) {
        return records.stream()
                .filter(s -> s.getMajor().equalsIgnoreCase(major))
                .toList();
    }
    
    // Sorting by CGPA
    public List<Student> getStudentsSortedByCGPA() {
        return records.stream()
                .sorted(Comparator.comparingDouble(Student::getCgpa).reversed())
                .toList();
    }
    
    // Filtering students with scholarships
    public List<Student> getStudentsWithScholarship() {
        return records.stream()
                .filter(s -> s.getScholarshipAmount() > 0)
                .toList();
    }
}
