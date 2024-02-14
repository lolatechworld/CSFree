# they are collection of unique data
myset = {3, 4, 5, 6}
print(myset)
# help(myset) to check other terms
urset = {7, 9, 5, 12} #to add extra data using set
print(myset.union(urset))
# print(myset urset) is used with he straight line inbetween
print(myset.intersection(urset)) # the commont data
print(myset & urset) # another way of getting the commont data
print(myset.difference) # it returns the diff of two or more set it appears in one than the other
print(myset - urset) # all element excatly in one set not the both
print(urset - myset) # all element excatly in one set not the both
print(myset.symmetric_difference(urset)) # data that are not common in both
mylist = [1, 2, 1, 3, 3, 5, 6]
print(set(mylist)) #picks each data either common or not.
