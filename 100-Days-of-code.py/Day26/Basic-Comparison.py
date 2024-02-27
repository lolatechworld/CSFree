# If the temperature is above 30 degrees Celsius, should we activate the cooling system?

temp = int(input("What is the temperature: "))
if temp > 30:
    print("Should we activate the cooling system?")
else:
    print("Temperature is below 30 degrees. Cooling system activation not required.")

# using the define function
def temp(temp_degree):

    if temp_degree > 30:
       return("Should we activate the cooling system?")
    else:
        return("Temperature is below 30 degrees. Cooling system activation not required.")
temp_degree = float(input("Enter the temperature in degrees Celsius: "))

print(temp(temp_degree))