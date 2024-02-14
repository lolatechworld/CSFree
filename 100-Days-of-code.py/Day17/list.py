# List is used to keep a set of data
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", 
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
                     "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",]
print(states_of_america)
# print positive index
print(states_of_america[4])
# print negative index
print(states_of_america[-1])
# to ulter a perticular data
states_of_america[1] = "pencilvania"
states_of_america.append("Hawaii") # to add an item to the end of your data
states_of_america.extend(["Hawaii", "Alabama", "Michigan", "Florida" ]) # to add mulitiple items to the list
print(states_of_america) 
