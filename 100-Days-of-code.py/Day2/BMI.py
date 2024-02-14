# Create a Python program that computes the (BMI) based on user input.
# The BMI considers both weight and height, providing an indication of body composition. 
# The BMI is determined by dividing a person's weight (in kilograms) by the square of their height

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Input user data
weight = float(input("Enter your weight (in kilograms): "))
height = float(input("Enter your height (in meters): "))

# Calculate BMI using the function
bmi = calculate_bmi(weight, height)

# Display the calculated BMI
print(f"Your BMI is: {bmi:.2f}")
