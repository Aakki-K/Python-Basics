# TODO 1: Question
"""
You are going to write a program that will select a random name from a list of names.
 The person selected will have to pay for everybody's food bill.

 Input :
 Angela, Ben, Jenny, Michael, Chloe

 Output :
 Michael is going to buy the meal today!
"""

# TODO 2: Import Zone
import random

# TODO 3: Welcome Code
print(f"\n***** Welcome to random meal payer ******\n")

# TODO 4: Input from user
Names_List = input("Enter the Names (Eg: john, tom, kim) : ").split(", ")

# TODO 5: Logic
No_of_People = len(Names_List)
Random_Number = random.randint(0, No_of_People - 1)

# TODO 6: Output
print(f"{Names_List[Random_Number]} is going to buy the meal today!")
















