#Write a Python function called find_primes that takes a positive integer n 
#as its parameter and returns a list containing all prime numbers less than or equal to n. 
#A prime number is a natural number greater than 1
# that is not a product of two smaller natural numbers.

#Finding prime numbers

#PSEUDOCODE
#A user defined functn taking in a parameter n.
#we are going to return all numbers starting from a particular number to n.
#Contains a list called prime.
#return prime

def calculate_primes(n):
    if n >= 1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
primes = []
def find_primes(n):
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1, 2)):
            primes.append(num)
    return primes

n = 20
overall = find_primes(n)
print(overall)

