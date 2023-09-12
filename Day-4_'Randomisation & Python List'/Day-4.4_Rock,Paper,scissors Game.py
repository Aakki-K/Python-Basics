# TODO 1: Question
"""
Rock, Paper & Scissors Game
"""

# TODO 2: Logos
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# TODO 3: Import Zone
import random

# TODO 4: Welcome Code
print("\nWelcome to Rock, Paper, Scissors Game with Computer\n")

# TODO 5: User input
User_input = input("Enter your choice 'R' for Rock, 'S' for Scissors' & 'P' for Papers : ").lower()

# TODO 6: Logic

# Computer
Choice_list = ["r", "p", "s"]
Comp_choice = random.choice(Choice_list)

# Stage 1 : Draw
if User_input == "r" and Comp_choice == "r":
    print("\nYou choose Rock")
    print(rock)
    print("Computer also choose Rock")
    print(rock)
    print("so, DRAW")
elif User_input == "p" and Comp_choice == "p":
    print("\nYou choose Paper")
    print(paper)
    print("Computer also choose Paper")
    print(paper)
    print("so, DRAW")
elif User_input == "s" and Comp_choice == "s":
    print("\nYou choose Scissors")
    print(scissors)
    print("Computer also choose Scissors")
    print(scissors)
    print("so, DRAW")

# Stage 2 : Win
elif User_input == "r" and Comp_choice == "s":
    print("\nYou choose Rock")
    print(rock)
    print("Computer choose Scissors")
    print(scissors)
    print("so, YOU WON.....")
elif User_input == "p" and Comp_choice == "r":
    print("\nYou choose Paper")
    print(paper)
    print("Computer choose Rock")
    print(rock)
    print("so, YOU WON.....")
elif User_input == "s" and Comp_choice == "p":
    print("\nYou choose Scissors")
    print(scissors)
    print("Computer choose Paper")
    print(paper)
    print("so, YOU WON.....")

# Stage 3: Lose
elif User_input == "r" and Comp_choice == "p":
    print("\nYou choose Rock")
    print(rock)
    print("Computer choose Paper")
    print(paper)
    print("so, YOU LOSE.....")
elif User_input == "p" and Comp_choice == "s":
    print("\nYou choose Paper")
    print(paper)
    print("Computer choose Scissors")
    print(scissors)
    print("so, YOU LOSE.....")
elif User_input == "s" and Comp_choice == "r":
    print("\nYou choose Scissors")
    print(scissors)
    print("Computer choose Rock")
    print(rock)
    print("so, YOU LOSE.....")
else:
    print(f"You choose {User_input}, which is inappropriate option")







