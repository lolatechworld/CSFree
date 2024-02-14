# create a python program that outputs 
# the years, days, and weeks 
# a user would live after collecting 
# their name, age, and years.

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
intend_years = int(input("Enter the years you intend to spend on earth: "))
gender = input("What is your gender: ")

print(f"{user_name}, the number of years you intend speding is {intend_years}")
days = intend_years - user_age
total_days = days * 365
total_weeks = days * 52
print(f"{user_name} you have a total of {total_days} days remaining")
print(f"{user_name} you have a total of {total_weeks} weeks remaining")  