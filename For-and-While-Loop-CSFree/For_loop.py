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
n = int(input("Enter a number :"))

for i in range(1, 13):
    result = n * i
    print(f"{n} x {i} = {result}")
    
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
    
# 5. Write a Python function that uses a for loop to count the number of vowels in a given word.
def count_vowels(word):
    #Counts the number of vowels in a given word using a for loop.

    vowels = "aeiou"
    vowel_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1

    return vowel_count
word = input("Enter a word: ")  
# Get user input for a more interactive experience
vowel_count = count_vowels(word)
print(f"The word {word} has {vowel_count} vowels.")

# 6. Generating a sequence of or find the factorial of a given numbers
n = int(input("Enter a number: "))
factorial_result = 1 # if factorial_result = 3
# 3*2*1
# 3*2*1
# 3*2*1 if the factorial result = (3 + 3)
for i in range(1, n + 1):
    factorial_result += i
print(f"The factorial on {n} is: {factorial_result} ")

# 7. Develop a program using a for loop to find the largest element in a list of numbers.

# 8. Create a Python script that utilizes a for loop to generate the Fibonacci sequence up to the 20th term.

# 9. Write a program that uses a for loop to print the reverse of a given string.

# 10. Develop a Python script that uses a for loop to find and print prime numbers within a given range.

# 11. Implement a program with a for loop to calculate the average of a list of numbers.