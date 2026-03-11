class DayTwo {

    // --- CONCEPT 2: VARIABLE TYPES ---
    // This is an Instance Variable (Belongs to the specific object)
    String studentName;
    
    // This is a Static Variable (Shared by all DayTwo objects)
    static String batchName = "PGCP-AI Feb 2026";

    // --- CONCEPT 3: CONSTRUCTORS ---
    // This is a Parameterized Constructor. It builds the object!
    public DayTwo(String name) {
        this.studentName = name; // Initializes the instance variable
    }

    // The main method: Where execution starts
    public static void main(String[] args) {
        
        System.out.println("--- Welcome to Day 2, " + batchName + " ---");

        // We use our Constructor to create a new Object
        DayTwo myProfile = new DayTwo("AI Architect");
        System.out.println("Student Name: " + myProfile.studentName);

        // --- CONCEPT 1: TYPE CASTING ---
        System.out.println("\n--- Type Casting Demo ---");
        
        // 1. Implicit (Widening): int (4 bytes) to double (8 bytes)
        int myInt = 100;
        double myDouble = myInt; // Automatic! No data loss.
        System.out.println("Original Int: " + myInt);
        System.out.println("Widened to Double: " + myDouble);

        // 2. Explicit (Narrowing): double (8 bytes) to int (4 bytes)
        double largeDecimal = 99.99;
        int narrowedInt = (int) largeDecimal; // Manual cast required! Data loss happens.
        System.out.println("Original Double: " + largeDecimal);
        System.out.println("Narrowed to Int (Notice the lost decimals!): " + narrowedInt);
    }
}