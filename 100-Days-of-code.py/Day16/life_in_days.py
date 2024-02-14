# Create a Python program that calculates and 
# outputs the number of days you have left 
# if you live until 100 years old. 
# The program should take your current age as input 

# def age():
name = input("Enter your name: ")
age = input("What is your current age: ")
days_lived = 100 - int(age)
days_remaining = days_lived * 365
print(f"{name} you have {days_remaining} days remaining.")