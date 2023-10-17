'''Write a program that calculates the Body Mass Index (BMI)
 from a user's weight and height with round figure output.
 BMI = Weight / height squared'''

#Code

print("Welcome to BMI Calculator")
Weight = float(input("Enter your Weight : "))
Height = float(input("Enter your Height : "))

BMI = Weight / (Height ** 2)
print(round(BMI))

