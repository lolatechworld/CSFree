# Define a class for a student in respect to oop
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print("Student name is:", self.name)
        print("Student age is:", self.age)
        print("Student sex is:", self.sex)
# Creating an instance (object) of the Student class
student1 = Student(name="Lola", age=15, sex="Female")

# Using the object to print student information
student1.print_info()


class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter student age: "))
        self.sex = input("Enter student sex: ")

    def print_info(self):
        print("Student name is:", self.name)
        print("Student age is:", self.age)
        print("Student sex is:", self.sex)

# Creating an instance (object) of the Student class
student1 = Student()

# Using the object to print student information
student1.print_info()

