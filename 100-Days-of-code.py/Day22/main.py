# this is the entry point to our program
# randrange(start, stop, step)
# randint(a, b) to genetate a random integer between a and b


import random_module
import random

print(random_module.pi) # it can be used to call out a specific data

random_integer = random.randint(1, 10)# whenever you run it, you get a random integer between the specified no 
print(random_integer) 

random_float = random.random()# whenever you run it, you get a random integer between the specified no 0-1
random_float * 5 #to print float from 0-5
print(random_float)

love_rate = random.randint(1, 100)
print(f"Your love rate is {love_rate}")