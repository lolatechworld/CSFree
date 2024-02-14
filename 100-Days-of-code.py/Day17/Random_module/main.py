import random
import my_module
# print(my_module.pi) # it will print out the value of the my_module

random_integer = random.randint(1, 10)
print(random_integer)

# 0.00000000 - 0.99999999
random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")