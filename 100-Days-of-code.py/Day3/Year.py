# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0: # its divisible by 4, it's a leap year
    if year % 100 == 0: # it's divisible by 4 and 100 it's not a leap year
            if year % 400 == 0: # it's divisible by 400, it's a leap year
            #      print("Leap year")
            # else:
                 print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")