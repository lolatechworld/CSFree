# Define a class for a simple Animal
class Student:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Student name is: ")

# Create instances (objects) of the Animal class
lion = Student(name="Dami")

# Use the objects
lion.make_sound()   # Output: Some generic animal sound
#Encapsulation: in oop the group related variables and functions that operate on them 