# TODO 1: Import Zone
import os
import random
from art import logo, vs
from Gamedata import Instagram_Keys, Instagram_Dictonary
from functions import Random_Item, Result

# TODO 2: Code
# printing logo
print(logo)

# Getting Random A & B
A = Random_Item(Instagram_Keys)
B = Random_Item(Instagram_Keys)
if B == A:
    while not B != A:
        B = Random_Item(Instagram_Keys)

# Asking Question
Guess = input(f"""
A. {A}
{vs}
B. {B}\n\n
Who has more followers on instagram? (A or B) : """).upper()

# User_Choice
if Guess == "A":
    User_Choice = A
elif Guess == "B":
    User_Choice = B

# Other_Option
if Guess == "A":
    Other_Option = B
elif Guess == "B":
    Other_Option = A

# Score
Score = 0

if Result(User_Choice, Other_Option, Instagram_Dictonary):
    Loop_on = True
    while Loop_on:
        os.system("cls") # Clear Screen
        print(logo) # Reprinting logo
        Score += 1 # Adding score
        print(f"You got it right, Your score is {Score}") # Printing score
        Instagram_Keys.remove(Other_Option)  # Removing Other option from Instagram keys
        Other_Option = Random_Item(Instagram_Keys) # Assigning new Other option
        # Making Sure User_Choice is not equal to Other_option
        if Other_Option == User_Choice:
            while not Other_Option != User_Choice:
                Other_Option = Random_Item(Instagram_Keys)
        # Taking User_Choice
        Guess = input(f"""
        A. {User_Choice}
        {vs}
        B. {Other_Option}\n\n
        Who has more followers on instagram? (A or B) : """).upper()

        # Reconfiguring User_choice
        Clone = User_Choice

        if Guess == "A":
            User_Choice = User_Choice
        elif Guess == "B":
            User_Choice = Other_Option
            Other_Option = Clone

        # Result
        if Result(User_Choice, Other_Option, Instagram_Dictonary):
            Loop_on = True
        else:
            os.system("cls")
            print(f"Game Over, Your answer is wrong & SCORE is {Score}")
            Loop_on = False

        if len(Instagram_Keys) == 2:
            os.system("cls")
            print(f"Game Over, You got all right & SCORE is {Score}, Congratulations")
            Loop_on = False
else:
    print("You got it wrong, YOU LOSE")






















