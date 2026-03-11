import java.util.Scanner;

public class evenorodd {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter number: ");
        int num = input.nextInt(); 
        if (num % 2 == 0) {
            System.out.println(num + " Even number.");
        } else {
            System.out.println(num + " Odd number.");
        }
        input.close();
    }
}