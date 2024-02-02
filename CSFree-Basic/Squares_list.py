#!/usr/bin/python3
# Generate the square of the members in a given list
numbers = [1, 2, 3, 4, 5]

for_numbers = []
# use a for loop
for number in numbers:
    for_numbers.append(number ** 2)
    
print(f"Before: {numbers}")
print(f"After: {for_numbers}")
print()
# use list comprehension "take each no of the list and do somthing to it."
compr_numbers = [number ** 2 for number in numbers] #used to create a new list in an original list 
print(f"After list comprehension: {compr_numbers}")
