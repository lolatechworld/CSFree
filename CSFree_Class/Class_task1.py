#pseudocode
# 1. Create a function that takes a list of numbers as input, and return the sum of all the elements in the list.
#define your function
#Function takes in a list
#add the elements of the list
#return sum 

def sum_numbers(lst=None):
    
    sum = 0
    for i in lst:
        sum = sum + i

    return sum
        
total = sum_numbers([1,2,3,4,5,6,7,8,9,10])
print(total)

def sum_numbers(lst=None):

    sum = 0
    for i in lst:
        #sum += i
        sum = sum + i

    return sum
        
total = sum_numbers([1,2,3,4,5,6,7,8,9,10])
print(total)

def sum_numbers(lst=None):
    total_sum = 0
    for i in lst:
        total_sum += i

    return total_sum

# Example usage:
total = sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(total)