# generate a random number and 
# use it to print out if the coin toss is head or tail.
import random
coin_toss = random.randint(0, 1)
if coin_toss == 1:
    print("Heads")
else:
    print("Tail")
