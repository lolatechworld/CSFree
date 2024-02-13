# Getting the value of the Key in my dic
mydict = {"maths":84, "government":92}
type(mydict)
print(mydict["government"])

# 1.for loop used to access value in the key
mydict = {"maths":84, "government":92}
for i in mydict:
    print(mydict[i])

# 2.for loop used to access the key in my dictionary
for subject in mydict.keys():
    print(subject)  

# 3.for loop using the keys to access value
for subject in mydict.values():
    print(subject)

# 4.for loop used to access the keys and value
for subject in mydict.items():
    print(subject)

# 5. another way in  the 
for subject, score in mydict.items():
    print(f"Subject = {subject} and Score = {score}")
