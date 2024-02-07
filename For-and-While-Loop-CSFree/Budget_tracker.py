#writing a code that tracts our budget project
balance = 0

print("Welcome to Techtians budget tracker select any of the options below: \n")
while True:
    print("1. Add Income")
    print("2. Add Expenses")
    print("3. View Balance")
    print("4. Exit")
    try:
        size = (input("Enter your size (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue # skip the rest of the loop and start OverflowError
    

    if size == 1:
        income_amount = float(input("Enter the income amount: "))
        balance += income_amount
        print(f"income of ${income_amount} added. Updated balance: ${balance}")

    elif size == 2:
        expense_amount = float(input("Enter the expenses amount: "))
        balance  -= expense_amount
        print(f"Expense of ${expense_amount} deducted.")

    elif size == 3:
        print(f"current balance ${balance}")

    elif size == 4:
        print("Exit the budget tracker program")
        break

    else:
        print("invalid size. Please enter a number between 1-4")