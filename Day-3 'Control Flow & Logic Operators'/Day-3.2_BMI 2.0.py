"""
Write a program that interprets the Body Mass Index (BMI) based
 on a user's weight and height.

It should tell them the interpretation of their BMI
 based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.
"""
# TODO 1: Exceptions
'''
Input :
 Weight = 85Kgs, Height = 1.75m
Output :
 85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.
'''

# TODO 2: Welcome Code
print(f"***** Welcome to BMI Calculator *****")

# TODO 3: Inputs
Weight = float(input("Enter your Weight in Kgs : "))
Height = float(input("Enter your Height in meters : "))

# TODO 4: Logic & Code
BMI = round(Weight / (Height ** 2))

if BMI <= 18.5:
    print(f"Your BMI is {BMI},so that you are 'Underweight'")
elif BMI <= 25:
    print(f"Your BMI is {BMI},so that you are 'Normal weight'")
elif BMI <= 30:
    print(f"Your BMI is {BMI},so that you are 'Slightly Overweight'")
elif BMI <= 35:
    print(f"Your BMI is {BMI},so that you are 'Obese'")
else:
    print(f"Your BMI is {BMI},so that you are 'Clinically Obese'")









