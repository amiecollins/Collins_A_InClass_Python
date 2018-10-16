# import random package so that we can generate random numbers
from random import randint

# choices is an array of game options
choices = ["Rock", "Paper", "Scissors"]

# computer makes a choice using a random integer
computer_choice = choices[randint(0,2)]

# print choice
print("Computer chooses: ", computer_choice)