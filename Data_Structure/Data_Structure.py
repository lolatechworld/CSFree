#Listing the no of element in a list
names = ["Ralph", "Dammi", "Milo", "Yusuf", "Tobi", "Ben", "Ella", 10]
numbers = {5, 2, 6, 8, 10}
list = {2024, "Dami", 5.5}
print(len(names))
print(len(numbers))
print(len(list))

#Arrange element to a list
print(sorted(numbers))



# to extend the list with another list
numbers.extend([2, 5])
print(numbers)
add_to_list = {21, 55, 100}
numbers.extend(add_to_list)
print(numbers)
