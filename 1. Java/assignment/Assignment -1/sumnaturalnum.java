import java.util.Scanner;

public class sumnaturalnum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter a num: ");
        int n = input.nextInt();
        
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum = sum + i;
        }
        System.out.println("Sum: " + sum);
    }
}