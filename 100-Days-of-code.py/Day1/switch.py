# Write a Python program that takes two inputs, 
# where the first input is stored in a variable called x, 
# and the second input is stored in a variable called y. 
# Your task is to switch the values stored in the variables x and y.
x = input()
y = input()

z = x
x = y
y = z

print(f"x: {x}")
print(f"y: {y}")
