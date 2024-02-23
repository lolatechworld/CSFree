import random

def get_random_name(names_string):

    if not names_string:
        raise ValueError("Input string cannot be empty.")

    # Split the string into a list of names, removing extra spaces
    names = names_string.strip().split(", ")

    if not names:
        raise ValueError("Input string must contain comma-separated names.")

    # Generate a random index within the valid range
    random_index = random.randint(0, len(names) - 1)

    # Return the randomly selected name
    return names[random_index]

# Example usage:
names = "milo, lola, Dami, Momo"
random_name = get_random_name(names)
print(random_name)  # Output: Bob (or any other random name from the list)
