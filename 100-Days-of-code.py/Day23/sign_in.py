print("Welcome to Tech-titans portal")
print("type ctrl d or ctrl c to quit the program")

user_data = {}  # Dictionary to store user data
storage = '.database'
import json

def signup():
    try:
        choice = input("Do you want to Sign Up or Sign In: ")

        if choice.lower() == 'sign up':
            user_info = {}  # Dictionary to store individual user's information
            choices = ["fullname", "username", "email"]

            # this senior boy is meant to only execute when choice is equal to sign up
            for usr_input in choices:
                user_info[usr_input] = input(f"Please Enter {usr_input}: ").strip()

            password = input("Create a password: ")
            user_info['password'] = password

            # Use the username as the key in the user_data dictionary
            user_data[user_info['username']] = user_info

            # open a file and write

            with open(storage, "w") as db:
                # db.write(str(user_data))
                json.dump(user_data, db, indent=2)

            print(f"Successfully signed up {user_info['username']}")
        elif choice.lower() == 'sign in':
           signin()
        else:
            print('Invalid Input! Try Again')

        continue_form = input("Do you want to signin? ")
        if continue_form.lower() == "signin":
            signup()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

def signin():

    try:
        signin_choice = input("Your username: ")
        pass_choice = input("Your password: ")

        with open(storage, "r") as db:
            user_data = json.load(db)
            if signin_choice in user_data:
                if user_data[signin_choice]['password'] == pass_choice:
                    print(f"Welcome back.{signin_choice}")
                else:
                    print("Incorrect password try again.")
            else:
                print("This user in not found sign up to Tech-titans portal")     
    except (KeyboardInterrupt, EOFError):
        print(f"Goodbye!")

try:
    signup()

except ValueError as ve:
    print("Error!")


# create a sign in button in the elif choce and use the 
# dictionary not the choices.
# create a big dictionary as key and the data as value.          
