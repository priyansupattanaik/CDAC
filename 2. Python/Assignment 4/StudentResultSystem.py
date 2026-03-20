class Student:
    def __init__(self):
        self.__marks = 0 
    
    def setMarks(self, m):
        if 0 <= m <= 100:
            self.__marks = m
            print(f"Marks set to: {m}")
        else:
            print("Error: Marks must be between 0 and 100")
    
    def getGrade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 40:
            return "C"
        else:
            return "Fail"

student = Student()
student.setMarks(85)
print(f"Grade: {student.getGrade()}")

student.setMarks(72)
print(f"Grade: {student.getGrade()}")

student.setMarks(45)
print(f"Grade: {student.getGrade()}")

student.setMarks(25)
print(f"Grade: {student.getGrade()}")

student.setMarks(150)