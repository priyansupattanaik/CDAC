from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}")
        print("Validating card details...")
        print("Connecting to payment gateway...")
        print(f"Payment of {amount} successful via Credit Card")
        print("Transaction ID: CC" + str(hash(amount))[:8])

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")
        print(f"Payment of {amount} successful via UPI")
        print("Transaction ID: UPI" + str(hash(amount))[:8])

print("Select Payment Method:")
print("1. Credit Card")
print("2. UPI")

choice = int(input("Enter your choice (1 or 2): "))
amount = float(input("Enter amount to pay: "))

if choice == 1:
    payment = CreditCardPayment()
else:
    payment = UPIPayment()

payment.pay(amount)