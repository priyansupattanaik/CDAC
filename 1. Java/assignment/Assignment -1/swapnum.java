import java.util.Scanner;

public class swapnum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter num1: ");
        int n1 = input.nextInt();
        
        System.out.print("Enter num2: ");
        int n2 = input.nextInt();
    
        n1 = n1 + n2;
        n2 = n1 - n2;
        n1 = n1 - n2;
        
        System.out.println("num1 = " + n1 + ", num2 = " + n2);
    }
}