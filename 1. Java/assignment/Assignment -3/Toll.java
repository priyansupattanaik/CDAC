import java.util.Scanner;
class TollBooth {
    String vehicleType;
    int numAxles;
    double distanceTraveled;
    private double tollFee;
    private double totalAmountDue;
    void calculateTollFee() {
        if (vehicleType.equalsIgnoreCase("truck")) {
            tollFee = 0.50 * numAxles * distanceTraveled;
        } 
        else {
            tollFee = 0.25 * numAxles * distanceTraveled;
        }
        totalAmountDue = tollFee + 2.00;
        System.out.println("Toll fee calculated successfully");
    }
    void generateBill() {
        if (tollFee == 0) {
            System.out.println("Please calculate toll fee first");
            return;
        }
        System.out.println("\n----- Toll Booth Bill -----");
        System.out.println("Vehicle Type: " + vehicleType);
        System.out.println("Number of Axles: " + numAxles);
        System.out.println("Distance Travelled: " + distanceTraveled + " miles");
        System.out.printf("Toll Fee: %.2f\n", tollFee);
        System.out.println("Processing Fee: 2.00");
        System.out.printf("Total Amount Due: %.2f\n", totalAmountDue);
    }
    static void showMenu() {
        System.out.println("\n1. Enter Vehicle Type (car, van, bus, truck)");
        System.out.println("2. Enter Number of Axles");
        System.out.println("3. Enter Distance Travelled");
        System.out.println("4. Calculate Toll Fee");
        System.out.println("5. Generate Bill");
        System.out.println("6. Exit");
        System.out.print("Enter your choice: ");
    }
}
public class Toll {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TollBooth toll = new TollBooth();
        int choice;
        do {
            TollBooth.showMenu();
            choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.print("Enter vehicle type: ");
                    toll.vehicleType = sc.nextLine();
                    break;
                case 2:
                    System.out.print("Enter number of axles: ");
                    toll.numAxles = sc.nextInt();
                    break;

                case 3:
                    System.out.print("Enter distance travelled (in miles): ");
                    toll.distanceTraveled = sc.nextDouble();
                    break;
                case 4:
                    toll.calculateTollFee();
                    break;
                case 5:
                    toll.generateBill();
                    break;
                case 6:
                    System.out.println("Thank you");
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        } while (choice != 6);
        sc.close();
    }
}
