# TODO 1: Getting Task
"""
write a program that calculates the highest score from a List of scores.
"""

# TODO 2: Module Import Zone


# TODO 3: Welcome Code
print(f"\nWelcome to Highest Score teller program")

# TODO 4: Input from User
Height_list_str = input("Enter the students height in cms (Eg: 180 190 152) : ").split(" ")

# TODO 5: Logic
# String to int
Height_list = []
for Str in Height_list_str:
    Height_list.append(int(Str))

# Highest
Highest_score = 0
for Score in Height_list:
    if Score > Highest_score:
        Highest_score = Score

# TODO 6: Output
print(f"The highest score is {Highest_score}")














