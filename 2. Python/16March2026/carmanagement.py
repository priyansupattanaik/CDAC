# Car Management
# #- car : object
# #- instance variables : speed, fuel
# #- instance method : accelerate(), brake(), speed()

class Car:
    def __init__(self, name, speed=0):
        self.name = name
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print(self.name, self.speed)

    def brake(self, amount):
        self.speed -= amount
        print(self.name, self.speed)

car1 = Car("Car A")
car1.accelerate(10)
print(car1.speed)
car1.brake(5)
car2 = Car("Car B", 20)
car2.accelerate(15)
print(car2.speed)
car2.brake(10)