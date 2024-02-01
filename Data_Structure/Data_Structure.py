#Listing the no of element in a list
names = ["Ralph", "Dammi", "Milo", "Yusuf", "Tobi", "Ben", "Ella", 10]
list = [2024, "Dami", 5.5]
numbers = [5, 2, 6, 8, 10] 

print(len(names))#to know the numbers of element in the list
print(len(list))
print(len(numbers))
numbers.append(20)#Adding one elements to the end of a list "e.g objects"
numbers.extend([7, 1])#To add iterable to the list or adding lists to your list and you can go over again
#or you initialize a variable, and add pass it to the existing list.
add_to_list = [21, 5, 55, 100]
numbers.extend(add_to_list)
numbers.insert(2, 90)#Insert also used to add elment to a list."by inserting an object before an index counting from 0"
numbers.insert(14, 102)
numbers.insert(0, 22)
numbers.pop()#To remove the last number in a list  with the index 
numbers.pop(2)#To remove a specific no in a list using their index
numbers.remove(20)#To remove a specific no on a list
del numbers[5]#Delete a no with its index
#Arrange element to a list
#print(sorted(numbers))
print(numbers)
print(len(numbers))

#to clear an entire list but you will still have an empty list
mynumbers = [4, 6, 9]
mynumbers.clear()
mynumbers
#To delete a total list, 
mynumbers = [5, 6, 7]

#Using Slicing
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#nums[start: end: step]
print(nums[0:2])
print(nums[0:6])
del nums[0:6:2]
nums.sort(reverse=True)#To start numbers of the end to the start
print(nums)
print(nums[::-1])#To reverse a string
s = "101"#To know if your string is in the right order
if s[::-1] == s:
    print("y")
    if s[::-1] ==s:
        print("True") 

#index means to return first index value
print(numbers)
print(numbers.index(90))#to know if a perticular no exist
numbers.index(5, 2)
numbers.append(100)
print(numbers)
new_numbers = numbers.copy()#To create a copy of the original list
print(new_numbers)