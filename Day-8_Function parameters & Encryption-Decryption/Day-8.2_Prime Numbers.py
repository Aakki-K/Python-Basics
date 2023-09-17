# TODO 1: Task
"""
You need to write a function that checks whether if the number passed into it is a prime number or not.
"""
# TODO 2: Welcome Code
print("**************** Welcome to Prime number checker *******************")

# TODO 3: Input from user
Number = int(input("Enter the number you wanna check : "))

# TODO 4: Logic
List = [0, 1, 2]
Sum = 0

if Number in List:
    print(f"It's a prime number.")
else:
    for n in range(2, Number - 1):
        if Number % n == 0:
            Sum += 1

if Sum == 0:
    print(f"It's a prime number.")
else:
    print(f"It's not a prime number.")
















