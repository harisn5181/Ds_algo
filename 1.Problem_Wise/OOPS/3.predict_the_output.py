class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student_details():
        print(self.name, end=" ")
        print(self.age)

    @staticmethod
    def isTeen(age):
        return age > 16


a = Student.isTeen(18)
s1=Student
s1.print_student_details()
print(a)