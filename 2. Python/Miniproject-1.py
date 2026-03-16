flowers = {
    "Rose": {"price": 10, "quantity": 100, "category": "Decorative"},
    "Tulip": {"price": 8, "quantity": 150, "category": "Bouquet"},
    "Sunflower": {"price": 12, "quantity": 80, "category": "Decorative"},
    "Lily": {"price": 15, "quantity": 60, "category": "Seasonal"},
    "Daisy": {"price": 5, "quantity": 200, "category": "Bouquet"},
    "Lotus": {"price": 20, "quantity": 50, "category": "Decorative"},
    "Orchid": {"price": 25, "quantity": 30, "category": "Exotic"},
    "Marigold": {"price": 6, "quantity": 180, "category": "Seasonal"}
}

def add_flower(flowers):
    name = (input("Enter flower name: "))
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Entetr category: ")

    flowers[name] = {"price" : price, "quantity" : quantity, "category" : category}
    print("Flower added successfully")

def update_flower(flowers):
    name = (input("Enter flower name to update: "))
    if name in flowers:
        price = int(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))
        category = input("Enter new category: ")

        flowers[name] = {"price" : price, "quantity" : quantity, "category" : category}
        print("Flower updated successfully")
    else:
        print("Flower not found")

def delete_flower(flowers):
    name = (input("Enter flower name to delete: "))
    if name in flowers:
        flowers.pop(name)
        print("Flower deleted successfully")
    else:
        print("Flower not found")

def search_flower(flowers):
    name = (input("Enter flower name to search: "))
    if name in flowers:
        print(f"Flower: {name}, Price: {flowers[name]['price']}, Quantity: {flowers[name]['quantity']}, Category: {flowers[name]['category']}")
    else:
        print("Flower not found")

def display_flowers(flowers):
    if not flowers:
        print("No flowers available")
        return
    for name, details in flowers.items():
        print(f"Flower: {name}, Price: {details['price']}, Quantity: {details['quantity']}, Category: {details['category']}")

def display_names(flowers):
    print("\nFlower Names:")
    for name in flowers.keys():
        print(name)

def display_details(flowers):
    print("\nPrice and Quantity:")
    for details in flowers.values():
        print(f"Price: {details['price']}, Quantity: {details['quantity']}")

def check_flowers(flowers):
    name = (input("Enter flower name: "))

    if name in flowers:
        print("Flower is available")
    else:        print("Flower is not available")

def count_flowers(flowers):
    print("Total number of flowers:", len(flowers))

def most_expensive(flowers):
    if not flowers:
        print("No flowers available")
        return
    
    flower = max(flowers, key=lambda x: flowers[x]['price'])
    print("Most expensive flower:", flower, flowers[flower])

def cheapest_flower(flowers):
    if not flowers:
        print("No flowers available")
        return
    
    flower = min(flowers, key=lambda x: flowers[x]['price'])
    print("Cheapest flower:", flower, flowers[flower])

def total_stock_value(flowers):
    total = 0

    for flower in flowers:
        price = flowers[flower]['price']
        quantity = flowers[flower]['quantity']
        total += price * quantity

    print("Total stock value:", total)

def low_stock(flowers):
    limit = int(input("Enter stock limit: "))
    print("Flowers with low stock:")
    for flower in flowers:
        if flowers[flower]['quantity'] < limit:
            print(flower, flowers[flower])

def sort_by_name(flowers):
    print("Flowers sorted by name:")
    for flower in sorted(flowers):
        print(flower, flowers[flower])

def sort_by_price(flowers):
    print("Flowers sorted by price:")
    
    sorted_flowers = sorted(flowers.items(), key=lambda x: x[1]['price'])
    for flower in sorted_flowers:
        print(flower)

def sell_flower(flowers):
    name = (input("Enter flower name to sell: "))
    quantity = int(input("Enter quantity to sell: "))

    if name in flowers:
        if flowers[name]['quantity'] >= quantity:
            flowers[name]['quantity'] -= quantity
            print(f"Sold {quantity} of {name}. Remaining stock: {flowers[name]['quantity']}")
        else:
            print(f"Not enough stock to sell. Available quantity: {flowers[name]['quantity']}")
    else:
        print("Flower not found")

def restock_flower(flowers):
    name = (input("Enter flower name to restock: "))
    quantity = int(input("Enter quantity to restock: "))

    if name in flowers:
        flowers[name]['quantity'] += quantity
        print(f"Restocked {quantity} of {name}. Current stock: {flowers[name]['quantity']}")
    else:
        print("Flower not found")

def expensive_flowers(flowers):
    price_limit = int(input("Enter price limit: "))
    result = [flower for flower in flowers if flowers[flower]['price'] > price_limit]
    print("Flowers above price limit:")
    for flower in result:
        print(flower, flowers[flower])

def clear_records(flowers):
    flowers.clear()
    print("All flower records cleared")

while True:
    print("\nFlower Management System")
    print("1. Add Flower")
    print("2. Update Flower")
    print("3. Delete Flower")
    print("4. Search Flower")
    print("5. Display All Flowers")
    print("6. Display Flower Names")
    print("7. Display Price and Quantity")
    print("8. Check Flower Availability")
    print("9. Count Total Flowers")
    print("10. Most Expensive Flower")
    print("11. Cheapest Flower")
    print("12. Total Stock Value")
    print("13. Flowers with Low Stock")
    print("14. Sort Flowers by Name")
    print("15. Sort Flowers by Price")
    print("16. Sell Flower")
    print("17. Restock Flower")
    print("18. Flowers Above Price Limit")
    print("19. Clear All Records")
    print("20. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_flower(flowers)
    elif choice == 2:
        update_flower(flowers)
    elif choice == 3:
        delete_flower(flowers)
    elif choice == 4:
        search_flower(flowers)
    elif choice == 5:
        display_flowers(flowers)
    elif choice == 6:
        display_names(flowers)
    elif choice == 7:
        display_details(flowers)
    elif choice == 8:
        check_flowers(flowers)
    elif choice == 9:
        count_flowers(flowers)
    elif choice == 10:
        most_expensive(flowers)
    elif choice == 11:
        cheapest_flower(flowers) 
    elif choice == 12:
        total_stock_value(flowers)
    elif choice == 13:
        low_stock(flowers)
    elif choice == 14:
        sort_by_name(flowers)
    elif choice == 15:
        sort_by_price(flowers)
    elif choice == 16:
        sell_flower(flowers)
    elif choice == 17:
        restock_flower(flowers)
    elif choice == 18:
        expensive_flowers(flowers)
    elif choice == 19:
        clear_records(flowers)
    elif choice == 20:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")