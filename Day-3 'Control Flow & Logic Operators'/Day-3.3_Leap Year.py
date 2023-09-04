# Question Code

"""
Write a program that works out whether if a given year is a leap year.
 A normal year has 365 days, leap years have 366, with an extra day
  in February.
"""
'''
Input :
2100
Output :
Not Leap year
'''
# TODO 1: Welcome Code
print(f"***** Check Leap Year *****")

# TODO 2: Input
Year = int(input("Enter the year : "))

# TODO 3: Logic & Output

if Year % 4 == 0:
    if Year % 100 != 0:
        if Year % 400 == 0:
            print(f"Leap Year")
    else:
        print(f"Not Leap Year")
else:
    print(f"Not Leap Year")











