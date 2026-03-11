import java.util.Scanner;

class ElectricityBill {
    String customerName;
    double unitsConsumed;
    double billAmount;
    
    public ElectricityBill(String customerName, double unitsConsumed) {
        this.customerName = customerName;
        this.unitsConsumed = unitsConsumed;
    }
    
    public void calculateBillAmount() {
        if (unitsConsumed <= 100) {
            this.billAmount = this.unitsConsumed * 5;
        } else if (unitsConsumed <= 300) {
            this.billAmount = 100 * 5 + (unitsConsumed - 100) * 7;
        } else {
            this.billAmount = 100 * 5 + 200 * 7 + (unitsConsumed - 300) * 10;
        }
    }
    
    public void displayBill() {
        System.out.println("Customer Name: " + customerName);
        System.out.println("Units Consumed: " + unitsConsumed);
        System.out.println("Total Bill Amount: Rs. " + billAmount);
    }
}

class ElectricityCalc {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter customer name: ");
        String Name = sc.next();
        System.out.println("Enter units consumed: ");
        double units = sc.nextDouble();
        
        ElectricityBill e = new ElectricityBill(Name, units);
        e.calculateBillAmount();
        e.displayBill();
    }
}