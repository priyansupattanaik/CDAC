class Employee:
    def calculateSalary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
    
    def calculateSalary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculateSalary(self):
        return self.hourly_rate * self.hours_worked

employees = [
    FullTimeEmployee("A", 5000),
    PartTimeEmployee("B", 20, 80),
    FullTimeEmployee("C", 6000),
    PartTimeEmployee("D", 25, 60)
]

for emp in employees:
    print(f"{emp.name}'s Salary: {emp.calculateSalary()}")