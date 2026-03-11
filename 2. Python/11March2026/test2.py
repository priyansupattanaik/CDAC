#Shop : 7 unit per product. 40% discount will be  implemented if multiple product is purchased.

Quantity = int(input("Enter the quantity of products you want to purchase: "))
unit_price = 7
total_price = Quantity * unit_price
if Quantity > 1:
    discount = total_price * 0.4
    total_price -= discount
print(f"Total price after discount: {total_price}")

