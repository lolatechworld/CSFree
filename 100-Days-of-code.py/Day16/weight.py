# calculate the bmi and output if it is overweight underwight or normal

def calculate_bmi(weight, height):
    return weight / (height * height)
# Enter your height in meters e.g., 1.55
height = float(input("What is your height: "))
weight = int(input("What is your weight: "))
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