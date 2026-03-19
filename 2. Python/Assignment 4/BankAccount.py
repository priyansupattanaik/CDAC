class BankAccount:
    def __init__(self, accountNumber, balance=0):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. New balance: Rs.{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def geBalance(self):
        return self.__balance
    
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)
print(f"Final balance: Rs.{account.geBalance()}")