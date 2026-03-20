from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

print("Choose shape:")
print("1. Circle")
print("2. Rectangle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    radius = float(input("Enter radius: "))
    shape = Circle(radius)
    print(f"Area of circle: {shape.area():.2f}")
else:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    shape = Rectangle(length, breadth)
    print(f"Area of rectangle: {shape.area():.2f}")