# Create a bankmanagement system in python using oops concepts, implement 3 methods withdraw, deposite, show balance, initialize the default values as when required. Display the content with multiple objects.

class BankAccount:
    def __init__(self, acc_number,balance = 0.0):
        self.acc_number = acc_number
        self.balance = balance

    def show(self):
        print("Account Number: ", self.acc_number)
        print("Balance: ", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ",amount)    

    def withdraw(self, amount):
            self.balance -= amount
            print("Withdrew ",amount,)

    def show_balance(self):
        print(self.name, "|", self.balance)

account1 = BankAccount("John Doe", 1000.0) 
account1.show() 
account2 = BankAccount("Jane Doe", 2000.0)
account2.show()
account3 = BankAccount("Alice Smith", 1500.0)
account3.show()