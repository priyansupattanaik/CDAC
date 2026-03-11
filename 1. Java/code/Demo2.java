class HelloWorld {
    
    // The main method: The starting point of the program
    public static void main(String[] args) {
        
        // 1. Printing Hello World
        System.out.println("Hello World! I am learning Java!");
        
        // 2. Doing Math Operations
        // We are using 'int', a primitive data type that stores whole numbers up to 4 bytes [11].
        int a = 10;
        int b = 5;
        
        int addition = a + b;
        int subtraction = a - b;
        int multiplication = a * b;
        
        // 3. Printing the results
        System.out.println("Addition of a + b = " + addition);
        System.out.println("Subtraction of a - b = " + subtraction);
        System.out.println("Multiplication of a * b = " + multiplication);
    }
}