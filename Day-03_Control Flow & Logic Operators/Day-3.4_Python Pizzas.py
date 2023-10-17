# Question Code

'''
Congratulations, you've got a job at Python Pizza.
Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
# TODO 1: Welcome Code
print("Welcome to Python Pizza Deliveries!")

# TODO 2: Inputs
size = input("What size pizza do you want? S, M, or L : ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N : ").lower()
extra_cheese = input("Do you want extra cheese? Y or N : ").lower()

# TODO 3: Logic
Bill = 0

# Pizza
if size == "s":
    Bill += 15
elif size == "m":
    Bill += 20
elif size == "l":
    Bill += 25

# Pepperoni
if size == "s" and add_pepperoni == "y":
    Bill += 2
elif (size == "m" or size == "l") and add_pepperoni == "y":
    Bill += 3

# Extra Cheese
if extra_cheese == 'y':
    Bill += 1


# TODO 4: Output
if Bill < 5:
    print(f"You have chosen Invalid options")
else:
    print(f"Your Total bill is {Bill}")



