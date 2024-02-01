#Listing the no of element in a list
names = ["Ralph", "Dammi", "Milo", "Yusuf", "Tobi", "Ben", "Ella", 10]
num = {5, 2, 6, 8, 10}
list = {2024, "Dami", 5.5}
print(len(names))
print(len(num))
print(len(list))


#Arrange element to a list
print(sorted(num))

#Adding elements in a list
num.append(20)
print(num)
print(len(num))

# To extend the list with other list
numbers.extend([2, 5])
print(numbers)
add_to_list = {21, 55, 100}
numbers.extend(add_to_list)
print(numbers)

#Insert a no to a list
numbers.insert(2, 90)
print(numbers)
#you can run len to know the numbers of element in the list
print(len(numbers))

#To remove the last number in a list 
numbers.pop(2)

#To remove a perticular no in a list
numbers.remove(5)

num = {5, 6,7}
#To delete a total list, 
del(num)
#Delete with indentation
del numbers [100]
print(numbers)

#Using Slicing
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(nums[0:2])
print(nums[0:6])

#To sort numbers of the same value
numbers.append(6)
numbers