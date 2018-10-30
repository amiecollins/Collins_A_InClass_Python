# import random package so that we can generate random numbers
from random import randint

# choices is an array of game options
choices = ["Rock", "Paper", "Scissors"]
player = False
c_lives = 3
p_lives = 3

# win / lose function
def winorlose(status):
    print("Called win or lose function")
    print("***************************")
    print("You", status, "! Would you like to play again?")
    choice = input("Y / N:")


    # reset lives
    if choice == "Y" or choice == "y":
        # change global variables
        global p_lives
        global c_lives
        global player

        p_lives = 3
        c_lives = 3
        player = False
    elif choice == "N" or choice == "n":
        print("You chose to quit!")
        print("***********************")
        exit()


# set up our loop
while player is False:

    # computer makes a choice using a random integer
    computer_choice = choices[randint(0, 2)]
    
    # set player to True by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper or Scissors?\n")

    print(player, "\n")

    # print computer choice
    print("Computer chooses: ", computer_choice)

    if player == computer_choice:
        print("Tie! You live to shoot another day")
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You lose! Paper covers Rock")
            p_lives -= 1
        else:
            print("You win!", player, "smashes", computer_choice)
            c_lives -= 1
    elif player == "Paper":
        if computer_choice == "Rock":
            print("You win!", player, "covers", computer_choice)
            c_lives -= 1
        else:
            print("You lose!", computer_choice, "cuts", player)
            p_lives -= 1
    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You lose!", computer_choice, "smashes", player)
            p_lives -= 1
        else:
            print("You win!", player, "cuts", computer_choice)
            c_lives -= 1
    elif player == "quit":
        exit()
    else:
        print("Check your spelling... thats not a valid choice\n")

    player = False

    if p_lives == 0:
        winorlose("lose")
    elif c_lives == 0:
        winorlose("won")

    # check for lives
    # if p_lives == 0:
    #    print("You lost all your lives, play again?\n")
    #     player = True
    # elif c_lives == 0:
    #     print("You win! The computer lost all it's lives. Play again?\n")
    #     player = True
        # set player to true to initiate quit prompt
    # if player is True:
    #     player = input("yes or no?\n")
    #     # if player says they want to continue
        # set player to false and reset lives
    #     if player == "yes" or player == "y":
    #         player = False
    #         p_lives = 3
    #         c_lives = 3
        # if player responds with anything else, end game by breaking loop
    
