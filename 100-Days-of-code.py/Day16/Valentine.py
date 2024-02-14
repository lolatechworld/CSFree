def calculate_compatibility():
    name = input("What's your name? ")
    print(f"Welcome {name}, today is Valentine get love now by using our val Calculator to see if you are compatable with your boo/bae...")

name1 = input("Enter the first name: " ) # What is your name?
name2 = input("Enter the second name: ") # What is their name?

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# # Calculate the first digit of compatibility
# first_digit = lower_names.count("t") + lower_names.count("r") + lower_names.count("u") + lower_names.count("e")

# # Calculate the second digit of compatibility
# second_digit = lower_names.count("l") + lower_names.count("o") + lower_names.count("v") + lower_names.count("e")


# Combine digits to get the compatibility percentage
compatibility_score = int(str(first_digit) + str(second_digit))

# Display compatibility result
print(f"\nCompatibility Result:")
print(f"{name1} and {name2}, your compatibility score is {compatibility_score} out of 100.")


# Determine and display match status
if (compatibility_score < 10) or (compatibility_score > 90):
    print("You go together like Ejiro and Testimony!")
elif (compatibility_score >= 40) and (compatibility_score <= 50):
    print("You are alright together. It's a potential match!")
else:
    print("Sparks are flying! You might have found your perfect match or be friends.")