class MathUtility {

    static int add(int a, int b){

        return a + b;
    }

    static int multiply(int a, int b){
        return a*b;
    }  
}

class Test3{
    public static void main(String[] args) {
        
        int sum = MathUtility.add(34,23);
        int product = MathUtility.multiply(32, 4);

        System.out.println("Sum: " +sum);
        System.out.println("Product: " +product);
    }
}
