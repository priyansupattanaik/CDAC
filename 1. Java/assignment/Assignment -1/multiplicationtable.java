import java.util.Scanner;

public class multiplicationtable {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter num: ");
        int num = input.nextInt();

        for (int i = 1; i <= 10; i++) {
            int result = num * i;
            System.out.println(num + " x " + i + " = " + result);
        }
        
        input.close();
    }
}