#!/usr/bin/python3
x = 40
y = 20

# Swap the values of x and y
z = x # this holds the initial vale x=40
x = y # x takes the value of y=20
y = z # y takes the value of z=40
print(f" x = {x} and y = {y}")
# using tuples to easily swap the numbers back 
x, y = y, x
print(f" x = {x} and y = {y}")