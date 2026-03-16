# # #OOPs: Object oriented programming.
# # It is a programming paradigm that uses objects and classes.
# # Instead of wriitng programs as a procedures, object oriented programming organize software into objects that contain both data and behaviour.

# # Ex: Laptop: Realtime entiity: object

# Advantages :
# 1. Code reusability
# - Classes can be reused using inheritance
# 2. Modularity:
# - Programs can be divided into smaller parts.
# 3. Security:
# - Data hiding can be implemented using encapsulaiton
# 4. Easy Maintenance:
# - Code becomes easy to update and manage.
# 5. Flexibility:
# - Supports polymorphism, allowing objects to be treated as instances of their parent class.
# 6. Real-world modeling:
# Programs resemble real world objects which provides real time solution.

#Class:
# - A class is a blueprint or template used to create objects.
# It defines:
# - variables
# - methods
# - behaviour of the concepts

# Syntax:
class ClassName:
    state1

# Ex:
class Cake:
    pass

#Object:
# - An object is an instance of a class.
# - It represents real world entity.

#Syntax:
# object_name = ClassName()

# Ex:

class Student:
    print("Hello")
    def display(self): # Defined function #self is a reference variable that refers to the current object.
        print("Getting Display")

s1 = Student() #object creation
s1.display() #calling the method using the object


# Importance of self keyword:
#self : is used to refer to the current instance (object) of the class.
# 1. Referes to current object.

#2. Used to access it as a instance variable.
# - allows method to access the variables of the object.

#3. Used as Instance and Local variable:
# Ex: 

# class Employee:
#     def __init__(self, name):
#         self.name = name
# name : parameter
# self.name : instance variable

#4. Used to call other method of same class:

#5. Every object can have their own data:

# - self represents the current object
# - It can be used to access instance variables adn methods
# - The first parameter in instance method must be self
# - It is automatically passed values when an object calls a method.

## Constructor:
# - A constructor is a special method that is automatically called when an object of a class is created.
# - Syntax:
# __init__()
# - Initialize object variables(attributes)
# - Assign initial values to object properties
# - Constructor executes when an object is created.

#Ex:

# class Abs:
#     def __init__(self): #Initialize the values

# Types of constructor:
#-----------------------
#1. Default constructor:
# - Runs automatically when an object is created.
# - Default values are assigned to the attributes.

#2. Parameterized Constructor
# - Parameteries constructor takes parameter to initialize object attributes
# - Values are passed during object creation.
# - Each object 

#Types of variables:
#1. Instance variable:
#2. Static variable: (class variable)
#3. Local variable:

#1. Instance variable:
# - Instance variables belongs to individual objects.
# - Each object has its own copy of instance variable.
# - Defined using self keyword inside the constructor or methods.

#keypoints:
#1. Created when object is created.
#2. It is stored inside the object memory.
#3. Accessed using 'self keyword'.
#4. Different object may have different values.

#2. Static variable (class variable):
# - Static variable belongs to the class .
# - They share all objects of the class.
# - declared inside the class but outside the method.

#Keypoints:
#1. One copy exist in the class.
#2. All objects share the same value.
#3. Accessed using class variable name.

#3. Local Variable:
#- variables declared inside the method
#- accessible only within the method

#Keypoints:
#-Temporary variable
#- Exist only during method execution
#- Not store in object memory

#Types of methods in OOPS:
#1. Instance method:
#2. Class method:
#3. Static method:

#1. Instance Method:
# - Instance method operates on instance varibles.
# - They require object creation

#Keypoints:
#1. First Parameter must be 'self'.
#2. Access instance variables 
#3. Called using objects

#Ex: Car Management
#- car : object
#- instance variables : speed, fuel
#- instance method : accelerate(), brake(), speed()

