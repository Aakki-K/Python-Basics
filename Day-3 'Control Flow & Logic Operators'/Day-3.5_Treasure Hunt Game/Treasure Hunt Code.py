"""
Treasure Island Game the flow chart is in this folder itself
"""

print('''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

Left_or_Right = input("Enter you wanna go Right road or Left road (R for Right & L for Left) : ").lower()
if Left_or_Right == "l":
    Swim_or_Wait = input(f"You wanna go Swim or Wait for boat (S for Swim & W for Wait) : ").lower()
    if Swim_or_Wait == "w":
        Door = input(f"Which door you wanna choose Red or Blue or Yellow (R for Red, B for Blue & Y for yellow) : ").lower()
        if Door == "r":
            print(f"Game Over, The door is had a fire & You burnt")
        elif Door == "b":
            print(f"Game Over, You have eaten by Beasts")
        elif Door == "y":
            print(f"You Won, Congratulations")
        else:
            print(f"Game Over, You have chosen improper option")
    else:
        print(f"Game Over, You have been eaten by crocodile")
else:
    print(f"Game Over, You fall into an hole")


















