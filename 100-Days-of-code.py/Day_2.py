# 1.two_digit_number = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# first_digit = int("two_digit_number: ")
# second_digit = int("two_digit_number: ")
# # Calculate the sum of the digits
# two_digit_number = first_digit + second_digit
# # Print the result
# print(two_digit_number)

first_digit = int(3)
second_digit = int(9)
# Calculate the sum of the digits
two_digit_number = first_digit + second_digit
# Print the result
print(two_digit_number)

####################################

# 2. Function to calculate BMI
height = 1.65
weight = 72

def calculate_bmi(height, weight):
    weight_as_int = int(weight)
    height_as_float = float(height)
    
    # Using the exponent operator **
    bmi = weight / (height ** 2)
    bmi = int(bmi)
    
    return bmi
result = calculate_bmi(height, weight)
print(result)

# 3.
age = input("what is your age? ")
# 🚨 Don't change the code above 👆
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
years_remaining = 90 - int(age)
weeks_remaining = years_remaining * 52
print(f"you have {weeks_remaining} weeks left")

age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")