# to delete an item in a tuple isnt allowed except you intend deleting the whole tuple 
# you cant add element to a tupple using the append
scores = (80, 50, 30, 40)
# Accessing the members of a tuple
# indexing
type(scores)
print(scores[0])
print(scores[:3]) # to get some set
print(scores[:-2])
# to get the element in a tupple
print(len(scores))
# but you can add a new set of tuple to the previous using concatination by creating a new variable
scores = scores + (20, 10)
print(scores)