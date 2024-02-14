# tells the user if they got head or tail

import random
random_number = random.randint(0, 1) # it generates a random integer

if random_number == 1:
    print("Heads")
else:
    print("Tails")