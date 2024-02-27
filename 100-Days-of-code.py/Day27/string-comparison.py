# "If the user input contains the word 'cancel,' should the transaction be aborted?"

user_input = input("Enter your transaction details: ")

if 'cancel' in user_input.lower():
    print("Transaction aborted.")
else:
    print("Transaction processed successfully.")


# Using a define function for the code above
def transaction_process(user_input):
    if 'cancel' in user_input.lower():
        return "Transaction aborted."
    else:
        return "Transaction processed successfully."

# Taking user input for transaction details
user_input = input("Enter your transaction details: ")

# Calling the defined function and printing the result
print(transaction_process(user_input))
