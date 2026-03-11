import java.util.Scanner;

public class factorialnum {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        System.out.print("Enter num: ");     
        int num = input.nextInt();        
        int factorial = 1;       
        for (int i = 1; i <= num; i++) {
            factorial = factorial * i;       
        }
        System.out.println("Factorial of " + num + ": " + factorial);
        
        input.close();
    }
}