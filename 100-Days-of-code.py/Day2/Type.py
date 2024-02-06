# Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name? "))
# type prevent error by checking whatever you put betw the () and gives you the type of data.
# when you are not very sure of a data type, you use the type function
print(type(num_char))
# type conversation or type casting is used to change a data type to another using str from int.
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
# is an integer but can be turned diff data types e.g float, string
a = 123
a = float(123)
a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+ str(100))
# you can use the type function to investigate the type of data you are working with
# and you can use functions like str, int or float to convert to that data type.