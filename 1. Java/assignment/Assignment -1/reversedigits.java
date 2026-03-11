import java.util.Scanner;

public class reversedigits {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        System.out.print("Enter num: ");
        
        int num = input.nextInt(); 
        int reversedNum = 0;
        
        while (num != 0) {
            
            int lastDigit = num % 10;
            reversedNum = (reversedNum * 10) + lastDigit;
            num = num / 10;    
        }
        System.out.println("Reversed num: " + reversedNum);
        
        input.close();
    }
}