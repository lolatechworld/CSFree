# Write a Python function called find_largest_number 
# that takes three numbers as parameters and returns 
# the largest among them. Don't use any built-in Python 
# functions like max().

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

def find_largest_number_to_return_smallest_number(num1, num2, num3):
    largest_number = 0  # Initializing largest_number
    middle_number = 0   # Initializing middle_number
    smallest_number = 0  # Initializing smallest_number

    if num1 > num2 and num1 > num3:
        largest_number = num1
        if num2 > num3:
            smallest_number = num3
            middle_number = num2
        else:
            smallest_number = num2
            middle_number = num3
    elif num2 >= num1 and num2 >= num3:
        largest_number = num2
        if num1 > num3:
            smallest_number = num3
            middle_number = num1
        else:
            smallest_number = num1
            middle_number = num3
    else:
        largest_number = num3
        if num1 > num2:
            smallest_number = num2
            middle_number = num1
        else:
            smallest_number = num1
            middle_number = num2
    
    return largest_number, middle_number, smallest_number

largest_number, middle_number, smallest_number = find_largest_number_to_return_smallest_number(num1, num2, num3)

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")
print(f"Largest to smallest numbers: {largest_number}, {middle_number}, {smallest_number}")

    
       
# def find_largest_number_to_return_smallest_number(num1, num2, num3):
#     largest_number = max(num1, num2, num3)
#     return largest_number

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# largest_number = find_largest_number_to_return_smallest_number(num1, num2, num3)

# print(f"The largest number among {num1}, {num2}, and {num3} is: {largest_number}")
# print(f"Largest to smallest numbers: {largest_number}, {middle_number}, {smallest_number}")