# TODO 1: Import Zone
import random
from Functions import Result

# TODO 2: Code
# Welcome Code
print("Welcome to Number Guessing game")
print("The number is in the range of 0 to 100")

# Choosing Difficulty
Difficulty = input("Enter the Difficulty level: Easy or Hard? : ").lower()

# Random_number
Random_number = random.randint(0, 100)

# Attempts for Difficulty & Code
Attempts = 0

if Difficulty == "easy":
    Attempts = 10
    Result(Attempts, Random_number)
elif Difficulty == "hard":
    Attempts = 5
    Result(Attempts, Random_number)
else:
    print("Choose the appropriate option")


















