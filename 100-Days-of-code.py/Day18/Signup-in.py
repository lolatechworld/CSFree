# As a new recruit, you have the opportunity to join our elite team. 
# Are you ready to embark on this thrilling journey?

# Please choose your path:
# 📝 Sign up: Become an official CyberSleuth and create your agent profile.
# 🔐 Sign in: Already a CyberSleuth? Log in to access the CyberNet.
# What details should we include in your agent profile? Enter 'fullname,' 'username,' 'email,' and 'password' to get started. Uncover the secrets and let the cyber adventure begin!

# Note: Your mission is our priority, and your details are confidential. Once you're in, you'll be part of an exclusive community. 🌐🔒"

print("Welcome to CyberSleuth team.")
print("Are you ready to embark on this thrilling journey?")
user_info = {}
user_container = []

while True:
    choice = input("Choose to sign up or sign in: ")
    choices = ["fullname", "username", "email", "password"]
    for user_input in choices:
        # define dictionary
        user_info[user_input] = input(f"please enter {user_input}: ")
    print(f"sucessfully signed up {user_info ['username']}")

    break
print(user_info)

