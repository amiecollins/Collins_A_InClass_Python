# import random package so that we can generate random numbers
from random import randint

# choices is an array of game options
choices = ["Rock", "Paper", "Scissors"]
player = False

# computer makes a choice using a random integer
computer_choice = choices[randint(0, 2)]

# print choice
print("Computer chooses: ", computer_choice)

# set up our loop
while player is False:
    # set player to True by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    print(player, "\n")

    if player == computer_choice:
        print("Tie! You live to shoot another day")
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You lose! Paper covers Rock")
        else:
            print("You win!", player, "smashes", computer_choice)
    elif player == "Paper":
        if computer_choice == "Rock":
            print("You win!", player, "covers", computer_choice)
        else:
            print("You lose!", computer_choice, "cuts", player)
    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "smashes", player)
        else:
            print("You win!", player, "cuts", computer_choice)
    elif player == "quit":
        exit()
    else:
        print("Check your spelling... thats not a valid choice\n")
    player = False
