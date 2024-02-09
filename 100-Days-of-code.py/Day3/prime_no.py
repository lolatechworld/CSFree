# Write a program that takes a positive integer as 
# input and determines whether it is a prime number. 
# Keep prompting the user until they enter a positive integer. 
# The program should print whether the entered number is prime or not.

def positive_int(prime_num):
    if prime_num <= 1:
        return False
    for i in range(2, int(prime_num**0.5) +1):
        if prime_num % i == 0:
            return False
        #for i in rage(2, int(4**0.5) +1)
        #number=5
        #for i in range(2, int(4**0.5) + 1)
        #for i in range(2, int(4**1/2) + 1)
        #for i in range(2, (sqrt4)+1)
        #for i in range(2, 3)
        #2
        
    return True
    
while True:
    user_int = input("Enter a positive integer: \n")

    if user_int.lstrip("-").isdigit():
        prime_num = int(user_int)

        if prime_num > 0:
            if positive_int(prime_num):
                print(f"{prime_num} is a prime number")
                break
            else:
                print(f"{prime_num} is not a prime number, please enter a prime number")
        else:
            print("Make sure it is a positive integer")
    else:
        print("Invalid input. Please enter a valid positive integer.")
