# TODO 1: Write the task
"""
You are going to write a program that calculates the average student height from a User input.
"""

# TODO 2: Welcome Code
print("\nWelcome to Average Height Calculator")

# TODO 3: Take input from User
Height_list_str = input("Enter the students height in cms (Eg: 180 190 152) : ").split(" ")

# TODO 4: Logic
# String to int
Height_list = []
for Str in Height_list_str:
    Height_list.append(int(Str))

# Summation of Heights & Count of students
Sum = 0
Count = 0
for Height in Height_list:
    Sum += Height
    Count += 1

# TODO 5: Output
Average = Sum / Count
print(f"The Average Height of students is {round(Average)}")













