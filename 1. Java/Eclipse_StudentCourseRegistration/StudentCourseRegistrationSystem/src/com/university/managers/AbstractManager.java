package com.university.managers;

import com.university.models.Person;
import java.util.List;
import java.util.function.Predicate;

public abstract class AbstractManager<T> {
    protected List<T> records;

    public abstract void add(T record);
    public abstract T findById(int id);
    public abstract void update(T record);
    public abstract void delete(int id);
    public abstract List<T> getAll();
    
    // Functional interface usage for filtering
    public List<T> filterRecords(Predicate<T> predicate) {
        return records.stream()
                .filter(predicate)
                .toList();
    }
    
    // Sorting with lambda expressions
    public List<T> sortRecords(java.util.Comparator<T> comparator) {
        return records.stream()
                .sorted(comparator)
                .toList();
    }
}
