# These code interprets the body mass index with a BMI calculatot. 

weight = int(input())
height = float(input())
bmi = weight / (height * height)
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


  # Write a Python program to interpret the health status of an individual based on their Body Mass Index (BMI). Prompt the user to enter their weight (in kilograms) and height (in meters), then calculate the BMI.