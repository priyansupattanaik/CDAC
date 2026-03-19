class StudentResultSystem:
    def __init__(self, marks):
        self.__marks = marks
    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        elif self.__marks >= 60:
            return "D"
        else:
            return "F"
        
student1 = StudentResultSystem(85)
print(f"Student's grade: {student1.calculate_grade()}")