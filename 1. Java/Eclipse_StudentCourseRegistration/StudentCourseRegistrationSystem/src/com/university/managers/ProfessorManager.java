package com.university.managers;

import com.university.models.Professor;
import com.university.exceptions.DuplicateProfessorIdException;
import com.university.exceptions.ProfessorNotFoundException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.function.Predicate;

public class ProfessorManager extends AbstractManager<Professor> {
    private int nextProfessorId = 2001;
    
    public ProfessorManager() {
        this.records = new ArrayList<>();
    }
    
    @Override
    public void add(Professor professor) {
        if (findById(professor.getProfessorId()) != null) {
            throw new DuplicateProfessorIdException("Professor with ID " + professor.getProfessorId() + " already exists");
        }
        professor.setPersonID(nextProfessorId++);
        records.add(professor);
    }

    @Override
    public Professor findById(int id) {
        return records.stream()
                .filter(p -> p.getProfessorId() == id)
                .findFirst()
                .orElse(null);
    }

    @Override
    public void update(Professor professor) {
        Professor existing = findById(professor.getProfessorId());
        if (existing == null) {
            throw new ProfessorNotFoundException("Professor with ID " + professor.getProfessorId() + " not found");
        }
        records.remove(existing);
        records.add(professor);
    }

    @Override
    public void delete(int id) {
        Professor professor = findById(id);
        if (professor == null) {
            throw new ProfessorNotFoundException("Professor with ID " + id + " not found");
        }
        records.remove(professor);
    }

    @Override
    public List<Professor> getAll() {
        return records;
    }
    
    // Stream API usage for searching
    public List<Professor> searchProfessorsByName(String name) {
        return records.stream()
                .filter(p -> p.getName().toLowerCase().contains(name.toLowerCase()))
                .toList();
    }
    
    public List<Professor> getProfessorsByDepartment(String department) {
        return records.stream()
                .filter(p -> p.getDepartment().equalsIgnoreCase(department))
                .toList();
    }
    
    // Sorting by experience
    public List<Professor> getProfessorsSortedByExperience() {
        return records.stream()
                .sorted(Comparator.comparingInt(Professor::getExperienceYears).reversed())
                .toList();
    }
}
