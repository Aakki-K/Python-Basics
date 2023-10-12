# TODO 1: Task
"""
Secret Auction program
"""

# TODO 2: Import Zone
import os
from art import logo

# TODO 3: Containers and Values
Bid = {}
Highest_value = 0

# TODO 4: Code
Continue = True
while Continue:
    os.system("cls")
    print(logo)
    print("*************** Welcome to Secret Auction Program ******************")
    Name = input("Bidder Name Please : ")
    Value = int(input("Enter the Bid Amount : $"))
    Bid[Name] = Value
    Stage = input("Enter N for next bidder and E to exit the bid : ").lower()
    if Stage == "e" or Stage == "exit":
        Continue = False

for Bidder in Bid:
    if Bid[Bidder] > Highest_value:
        Highest_value = Bid[Bidder]
        Bid_winner = Bidder


print(f"The Bid winner is {Bid_winner} with the highest bid of ${Highest_value}")
























