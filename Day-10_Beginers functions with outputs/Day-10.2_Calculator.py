# TODO 1: Task
"""
Calculator
"""

# TODO 2: Import Zone
from art import logo
import os

# TODO 3: Container Zone
operation = ["+", "-", "*", "/", "%"]

# TODO 4: Function Zone
def Math(First_Number, Second_Number, Operater):
    """The funtion performs basic math operations"""
    if Operater == "+":
        return First_Number + Second_Number
    elif Operater == "-":
        return First_Number - Second_Number
    elif Operater == "*":
        return First_Number * Second_Number
    elif Operater == "/":
        return First_Number / Second_Number
    elif Operater == "%":
        return First_Number % Second_Number
    else:
        return "Please choose the appropriate operation"

# TODO 5: Code
print(logo)
Loop_1 = True
while Loop_1:
    first_number = float(input("Enter the first number : "))
    Loop_2 = True
    while Loop_2:
        operator = input("Enter the Operation (+, -, *, /) : ")
        second_number = float(input("Enter the second number : "))
        if operator in operation:
            Value = round(Math(first_number, second_number, operator), 2)
            print(Value)

            Continue = input(f"Enter 'C' to continue with {Value}, 'N' to new calculation & 'E' to Exit Calculator : ").lower()
            if Continue == "e":
                Loop_2 = False
                Loop_1 = False
            elif Continue == "n":
                Loop_2 = False
                os.system("cls")
                print(logo)
            elif Continue == "c":
                first_number = Value
            else:
                Loop_2 = False
                Loop_1 = False
                os.system("cls")
                print(logo)
                print("Invalid option")
        else:
            print("Specify appropriate Operator")
            Loop_2 = False
            Loop_1 = False























