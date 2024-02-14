# Ass. create a program that calculates the bmi using dic
# with for loop takes date and height
# using update to update your dic
# bmi = {"weight": 70, "height": 1.72}
# bmi.pop("weight") used to remove

# Initialize an empty dictionary to store BMI data
bmi_data = {}

# Define the number of entries
num_entries = int(input("Enter the number of BMI entries: "))

# Use a for loop to input data and calculate BMI
for entry_num in range(1, num_entries + 1):
    date = input(f"Enter date for entry #{entry_num} (YYYY-MM-DD): ")
    weight = float(input("Enter weight (in kg): "))
    height = float(input("Enter height (in meters): "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Update the dictionary with BMI data
    bmi_data[date] = bmi

# Print the BMI data dictionary
print("\nBMI Data:")
for date, bmi in bmi_data.items():
    print(f"{date}: BMI = {bmi:.2f}")
