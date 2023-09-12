# TODO 1: Task
"""
Create the Py-Password Generator, which takes the input of no. of letters symbols & numbers
& Generate Strong password
"""

# TODO 2: Module import Zone
import random

# TODO 3: welcome code
print(f"\n Welcome to Py-Password Generator")

# TODO 4: Input from user
Letters = int(input("Enter the No. of letters you want in your Password : "))
Symbols = int(input("Enter the No. of Symbols you want in your Password : "))
Numbers = int(input("Enter the No. of Numbers you want in your Password : "))

# TODO 4: Logic
# Letter, numbers & symbol List
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Password List
Password_list = []
for n in range(0, Letters):
    Password_list.append(random.choice(letters))
for n in range(0, Symbols):
    Password_list.append(random.choice(symbols))
for n in range(0, Numbers):
    Password_list.append(random.choice(numbers))

random.shuffle(Password_list)
Final_Password = ""
for n in Password_list:
    Final_Password += n

# TODO 5: Output
print(Final_Password)















