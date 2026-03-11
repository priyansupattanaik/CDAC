import java.util.Scanner;

class TelephoneBill {
    
    String customerName;
    String phoneNumber;  
    int numberOfCalls;
    float durationOfCalls;
    float billAmount;

    public TelephoneBill(String customerName, String phoneNumber, int numberOfCalls, float durationOfCalls)
    {
        this.customerName = customerName;  
        this.phoneNumber = phoneNumber;    
        this.numberOfCalls = numberOfCalls;
        this.durationOfCalls = durationOfCalls;
    }

    public void calculateBill(){

        float callCharge = 0;

        
        float minDuration = durationOfCalls;
        if (minDuration < 1) {
            minDuration = 1;
        }

        if (numberOfCalls <= 100) {
            callCharge = numberOfCalls * 0.50f;
        } else {
            callCharge = 100 * 0.50f + (numberOfCalls - 100) * 0.25f;
        }

        this.billAmount = 10 + callCharge;  

    }

    public void displayBill(){
        System.out.println("Customer Name: " + customerName);
        System.out.println("Phone Number: " + phoneNumber);  
        System.out.println("Number of Calls: " + numberOfCalls);
        System.out.println("Duration of Calls: " + durationOfCalls + " minutes");
        System.out.println("Total Bill Amount:" + billAmount);  

    }
}

class TelephoneBillCalc {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Customer Name: ");
        String name = sc.nextLine();
        System.out.println("Enter Phone Number: ");
        String phone = sc.nextLine();  
        System.out.println("Enter Number of Calls Made: ");
        int calls = sc.nextInt();
        System.out.println("Enter Duration of Calls: ");
        float duration = sc.nextFloat();

        TelephoneBill teleBill = new TelephoneBill(name, phone, calls, duration);
        teleBill.calculateBill();
        teleBill.displayBill();
        
    }

}