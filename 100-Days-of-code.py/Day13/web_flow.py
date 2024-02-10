# We are creating a sign up or sign in form for our website
# create a prompt to either sign in or sign up
# if the user chooses to sign up collect the user info
# if they choose to sign in, only ask fot their username and password 
# create a program that 

print("Welcome to TechTitans portal")
user = []
while True:
    user = input("Do you want to sign up or sign in: ")

    if user.lower() == "sign up":
        name = input("Enter your username: ")
        username = input("Enter your desired user name: ") 
        password = input("Enter your desired password: ")
        email = input("Enter your email address: ")
        user.append({"Name": name, "Username": username, "Email": email, "Password": password})
        
        print(f"Hello {name}, your account has been created.")

        user_sign = input("Do you want to proceed in signing in? Y/N: ")
        if user_sign.lower() == 'Y': 
            enter_username = input("Enter your username: ")
            enter_password = input("Enter your password: ")
            for user in user:
                if user["username"] == enter_username and enter_password["password"] == password:
                    print(f"Welcome {name} you are signed in.")
                    break
        else:
            print("invaid username or password. Please try again.")    
    elif user.lower == "sign in":
        username = input("Enter your user name: ") 
        password = input("Enter your password: ")
        
        for user in user:
            if user["username"] == enter_username and enter_password["password"] == password:
                print(f"Welcome back, {name} you are signed in.")
                break
        else:
            print("Invalid username or password. Please try again.")
    else:
        print("Invalid input")
