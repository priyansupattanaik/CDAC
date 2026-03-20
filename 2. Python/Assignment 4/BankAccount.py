class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__accountNumber = account_number
        self.__balance = balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Error: Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrawn: {amount}. New balance: {self.__balance}")
            else:
                print("Error: Insufficient balance")
        else:
            print("Error: Withdrawal amount must be positive")
    
    def getBalance(self):
        return self.__balance

account = BankAccount("ACC12345", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000) 
print(f"Final balance: {account.getBalance()}")