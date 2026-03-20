class Vehicle:
    def __init__(self, speed, fuel_type):
        self.speed = speed
        self.fuel_type = fuel_type
    
    def display(self):
        print(f"Speed: {self.speed} km/h, Fuel Type: {self.fuel_type}")

class Car(Vehicle):
    def __init__(self, speed, fuel_type, car_type):
        super().__init__(speed, fuel_type)
        self.car_type = car_type

    def display(self):
        super().display()
        print(f"Car Type: {self.car_type}")

class Bike(Vehicle):
    def __init__(self, speed, fuel_type, color):
        super().__init__(speed, fuel_type)
        self.color = color

    def display(self):
        super().display()
        print(f"Color: {self.color}")

car = Car(180, "Petrol", "Sedan")
bike = Bike(120, "Petrol", "Blue")

print("Car Details:")
car.display()

print("Bike Details:")
bike.display()