# 1. program uses a for loop to print the first 10 natural numbers.
natural_number = 0
for n in range (11):
    natural_number = n
    print(natural_number)

# 2. program that uses a for loop to calculate the sum of the first 50 even numbers.
sum_even_no = 0
for no in range (2, 101, 2):
    sum_even_no += no
    print(sum_even_no)
    print("sum of the first 50 even no:", sum_even_no) 

# 3. Python script that utilizes for loop to print the multiplication table for a given number, e.g7.
for multiplication_no in range(7):
    multiplication_no *= 7
    print("multiplication_no of 7 is: ", multiplication_no)

# 4. write a Python program with a for loop to find and print the factorial of a given number.
# Function to calculate factorial using a for loop
def calculate_factorial(f):
    factorial_result = 1

    # Using a for loop to calculate the factorial
    for no in range(1, f + 1):
        factorial_result *= no

    return factorial_result

# Get input from the user
number = int(input("Enter a number: "))

# Check if the input is non-negative
if number < 0:
    print("Factorial is undefined for negative numbers.")
else:
    # Calculate and print the factorial
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")
    
