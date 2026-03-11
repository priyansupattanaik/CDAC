public class Program {
    public static void main(String[] args) {
        Person p = new Employee("Alice", 30, 101, 75000.0f); 
        
        // 2. DYNAMIC METHOD DISPATCH
        p.printRecord(); 
        
        Employee emp = (Employee) p; 
    }
}