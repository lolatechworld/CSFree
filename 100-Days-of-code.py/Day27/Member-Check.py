# If a student's name is not on the registered list, should they be allowed to enter the exam hall?

# this code above gives room for user to register the students
registered_students = []
registered_students = input("Enter registered_students: ")
student_name = input("Enter your name: ")

if student_name.lower() in registered_students:
    print(f"Welcome, {student_name}! You are registered.")
else:
    print(f"Sorry, {student_name} is not on the registered list. Entry denied.")


# the line of code below already have student registered names
registered_students = ["Lola", "Noah", "John"]

student_name = input("Enter your name: ")

if student_name.lower() in registered_students:
    print(f"Welcome, {student_name}! You are registered.")
else:
    print(f"Sorry, {student_name} is not on the registered list. Entry denied.")

