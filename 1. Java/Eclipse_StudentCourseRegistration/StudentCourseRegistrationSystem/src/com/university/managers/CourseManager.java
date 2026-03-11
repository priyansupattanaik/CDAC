package com.university.managers;

import com.university.models.Course;
import com.university.exceptions.CourseNotFoundException;
import com.university.exceptions.DuplicateCourseCodeException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;

public class CourseManager extends AbstractManager<Course> {
    private int nextCourseId = 3001;
    
    public CourseManager() {
        this.records = new ArrayList<>();
    }
    
    @Override
    public void add(Course course) {
        if (findById(course.getCourseCode()) != null) {
            throw new DuplicateCourseCodeException("Course with code " + course.getCourseCode() + " already exists");
        }
        course.setCourseCode(course.getCourseCode());
        records.add(course);
    }

    @Override
    public Course findById(int id) {
        return records.stream()
                .filter(c -> c.getCourseCode().equals(String.valueOf(id)))
                .findFirst()
                .orElse(null);
    }
    
    // Overloaded method to find by course code
    public Course findById(String courseCode) {
        return records.stream()
                .filter(c -> c.getCourseCode().equalsIgnoreCase(courseCode))
                .findFirst()
                .orElse(null);
    }

    @Override
    public void update(Course course) {
        Course existing = findById(course.getCourseCode());
        if (existing == null) {
            throw new CourseNotFoundException("Course with code " + course.getCourseCode() + " not found");
        }
        records.remove(existing);
        records.add(course);
    }

    @Override
    public void delete(int id) {
        Course course = findById(id);
        if (course == null) {
            throw new CourseNotFoundException("Course with ID " + id + " not found");
        }
        records.remove(course);
    }

    @Override
    public List<Course> getAll() {
        return records;
    }
    
    // Stream API usage for searching
    public List<Course> searchCoursesByName(String name) {
        return records.stream()
                .filter(c -> c.getCourseName().toLowerCase().contains(name.toLowerCase()))
                .toList();
    }
    
    public List<Course> getCoursesByDepartment(String department) {
        return records.stream()
                .filter(c -> c.getDepartment().equalsIgnoreCase(department))
                .toList();
    }
    
    // Sorting by credits
    public List<Course> getCoursesSortedByCredits() {
        return records.stream()
                .sorted(Comparator.comparingInt(Course::getCredits).reversed())
                .toList();
    }
    
    // Filtering available courses
    public List<Course> getAvailableCourses() {
        return records.stream()
                .filter(Course::isAvailable)
                .toList();
    }
}
