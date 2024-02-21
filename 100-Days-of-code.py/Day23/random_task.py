# Generate two random numbers between 1 and 100. 
# Ask the user to calculate their sum.

import random

random_a = random.randint(1, 100)
random_b = random.randint(1, 100)

random_sum = (random_a + random_b)
print(random_sum)


# Randomly shuffle the letters of a word 
# and ask the user to unscramble it to form the original word.

# import random

# def scramble(word):
#     original_word = input("your word: ")
# shuffled_word = random.sample(word, len(original_word))

# user_guess = input("Enter your guess here: ")
