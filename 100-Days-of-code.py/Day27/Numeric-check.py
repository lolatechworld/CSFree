# If the account balance falls below $100, should an alert be triggered?

account_name = input("Enter your account name: ")
account_balance = int(input("Enter your account balance: "))

if account_balance >= 100:
    print(f"{account_name} your a total balance of ${account_balance}")
else:
    print(f"Alert! {account_name}, your account balance is below $100.")


# Using a define function for the code above
account_name = input("Enter your account name: ") 

def balance(account_balance):

    if account_balance >= 100:
       return(f"{account_name} your a total balance of ${account_balance}")
    else:
        return(f"Alert! {account_name}, your account balance is below $100.")
account_balance = int(input("Enter your account balance: "))

print(balance(account_balance))