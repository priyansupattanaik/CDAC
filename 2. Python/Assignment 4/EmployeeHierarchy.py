class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Employee):
    def __init__(self, id, name, bonus):
        super().__init__(id, name)
        self.bonus = bonus
    
    def display(self):
        super().display()
        print(f"Bonus:{self.bonus}")

class Developer(Employee):
    def __init__(self, id, name, programming_language):
        super().__init__(id, name)
        self.programming_language = programming_language
    
    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

manager = Manager(101, "A", 5000)
developer = Developer(102, "B", "Python")

manager.display()
developer.display()