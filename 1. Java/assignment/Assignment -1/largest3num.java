import java.util.Scanner;

public class largest3num {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        System.out.print("Enter num1: ");
        int num1 = input.nextInt(); 
        System.out.print("Enter num2: ");
        int num2 = input.nextInt();
        System.out.print("Enter num3: ");
        int num3 = input.nextInt();

        if (num1 > num2 && num1 > num3) {
            System.out.println("The largest num is: " + num1);
        } else if (num2 > num1 && num2 > num3) {
            System.out.println("The largest num is: " + num2);
        } else if (num3 > num2 && num3 > num1) {
            System.out.println("The largest num is: " + num3);
        }
        else if (num1==num2 && num1==num3){
            System.out.println("all numbers equal");
        }
    }
}