# TODO 1: Task
""" Hangman Game"""

# TODO 2: Module Import Zone
from Art import logo
from Art import stages
import random
import os

# TODO 3: Welcome Code
print(logo)
print("************** Guess the Fruit ****************")

# TODO 4: Data
# Fruit list & Random fruit selection
Fruit_list = ["mango", "orange", "banana", "apple", "grapes", "Watermelon", "kiwi", "pineapple", "strawberry", "avocado", "pomegranate"]
Fruit = random.choice(Fruit_list)

# Displaying no. of blanks equal to length of fruit
Blanks = ""
Blanks_list = []
for n in range(0, len(Fruit)):
    Blanks_list.append("_")
for n in Blanks_list:
    Blanks += n
    Blanks += " "

Already_guessed_word = []
Wrong_answer = 0
Game_On = True
while Game_On:
    os.system("clear")
    print(Blanks)
    Word = input("Guess word : ")
    if Word in Fruit and (Word not in Already_guessed_word):
        for n in range(len(Fruit)):
            if Fruit[n] == Word:
                Blanks_list[n] = Word
        Blanks = ""
        for n in Blanks_list:
            Blanks += n
            Blanks += " "
        Already_guessed_word.append(Word)
    else:
        Wrong_answer += 1
        print(stages[7 - Wrong_answer])

    if Wrong_answer == 7:
        print("Sorry, You lost the Game ")
        Game_On = False
    elif "_" in Blanks_list:
        Game_On = True
    else:
        print("Congratulations, You won the Game ")
        Game_On = False




















