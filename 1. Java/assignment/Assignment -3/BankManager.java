import java.util.Scanner;
class BankAccount {
    String name;
    int accountNumber;
    double balance;

    BankAccount(String name, int accountNumber) {
        this.name = name;
        this.accountNumber = accountNumber;
        this.balance = 0;
    }
    void deposit(double amount) {
        this.balance = this.balance + amount;
        System.out.println("Deposit successful");
    }
    void withdraw(double amount) {
        if (amount <= this.balance) {
            this.balance = this.balance - amount;
            System.out.println("Withdrawal successful");
        } 
        else {
            System.out.println("Insufficient balance");
        }
    }
    void displayBalance() {
        System.out.println("Current Balance: " + this.balance);
    }
    void displayInfo() {
        System.out.println("Account Holder Name: " + this.name);
        System.out.println("Account Number: " + this.accountNumber);
        System.out.println("Balance: " + this.balance);
    }
}
public class BankManager {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        BankAccount account = null;
        int nextAccountNumber = 1001;
        int choice;
        do {
            System.out.println("\n1. Create Account");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Check Balance");
            System.out.println("5. Display Account Info");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();
            switch (choice) {
                case 1:
                    System.out.print("Enter Account Holder Name: ");
                    String name = sc.nextLine();
                    account = new BankAccount(name, nextAccountNumber);
                    System.out.println("Account created successfully");
                    System.out.println("Your Account Number is: " + nextAccountNumber);
                    nextAccountNumber++;
                    break;

                case 2:
                    if (account == null) {
                        System.out.println("No account found");
                    } 
        else {
                        System.out.print("Enter Account Number: ");
                        int accNo = sc.nextInt();
                        if (accNo == account.accountNumber) {
                            System.out.print("Enter amount to deposit: ");
                            double amount = sc.nextDouble();
                            account.deposit(amount);
                        } else {
                            System.out.println("Invalid account number");
                        }
                    }
                    break;
                case 3:
                    if (account == null) {
                        System.out.println("No account found");
                    } 
        else {
                        System.out.print("Enter Account Number: ");
                        int accNo = sc.nextInt();
                        if (accNo == account.accountNumber) {
                            System.out.print("Enter amount to withdraw: ");
                            double amount = sc.nextDouble();
                            account.withdraw(amount);
                        } else {
                            System.out.println("Invalid account number");
                        }
                    }
                    break;
                case 4:
                    if (account == null) {
                        System.out.println("No account found");
                    } else {
                        System.out.print("Enter Account Number: ");
                        int accNo = sc.nextInt();
                        if (accNo == account.accountNumber) {
                            account.displayBalance();
                        } 
else {
                            System.out.println("Invalid account number");
                        }
                    }
                    break;
                case 5:
                    if (account == null) {
                        System.out.println("No account found");
                    } 
        else {
                        System.out.print("Enter Account Number: ");
                        int accNo = sc.nextInt();
                        if (accNo == account.accountNumber) {
                            account.displayInfo();
                        } else {
                            System.out.println("Invalid account number");
                        }
                    }
                    break;
                case 6:
                    System.out.println("Thank you");
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        } while (choice != 6);
    }
}
