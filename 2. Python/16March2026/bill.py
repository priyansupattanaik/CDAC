#Create an application for billing for calculating bill. Calculate billby adding 18% GST to the total ammount and print final bill amount.

class Bill:
    def __init__(self, total_amount = 0.0):
        self.total_amount = total_amount

    def calculate_bill(self, price):
        tax = price * 0.18
        final_amount = price + tax
        return tax, final_amount

total_amount = float(input("Enter the total amount: "))
bill = Bill(total_amount)
gst, final_amount = bill.calculate_bill(total_amount)

print("Total Amount: ", total_amount)
print("GST (18%): ", gst)
print("Final Bill Amount: ", final_amount)