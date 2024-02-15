def treasure_island_game():
    print("Welcome to Treasure Island.")
    name = input("Enter your name: ")
    print(f"{name}, your mission is to find the treasure.")

    choice1 = input("Do you want to go left or right: ")
    if choice1.lower() == "left":
        choice2= input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()

        if choice2 == "wait":
            choice3 = input("You have arrive at the island safely. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?").lower()

            if choice3 == "red":
                print("It's a room full of fire. Game Over.")
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
            elif choice3 == "blue":
                print("You are eaten by beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You are attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")

