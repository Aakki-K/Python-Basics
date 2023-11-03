# TODO 1: Import Zone
from Project_Data import Water, Milk, Coffee, Expresso, Latte, Cappuccino
from functions import Enough_Money, Enough_Resources

# TODO 2: Code
# Resources
Water_Quantity = Water
Milk_Quantity = Milk
Coffee_Quantity = Coffee

# Asking the Type of Coffee
Loop_on = True
while Loop_on:
    Coffee = input("Enter the Coffee (Expresso, Latte, Cappuccino) : ").lower()
    if Coffee == "report":
        print(f"Water : {Water_Quantity}\nMilk : {Milk_Quantity}\nCoffee : {Coffee_Quantity}")
    elif Coffee == "expresso":
        if Enough_Money(Expresso["Cost"]):
            if Enough_Resources(Water_Quantity, Milk_Quantity, Coffee_Quantity, Expresso["Water"], Expresso["Milk"], Expresso["Coffee"]):
                Water_Quantity -= Expresso["Water"]
                Milk_Quantity -= Expresso["Milk"]
                Coffee_Quantity -= Expresso["Coffee"]
                print("Have your Expresso ☕\n\n")
            else:
                print("\nThe Machine dont have resources in enough quantity to make the demanded coffee try some other & also have your Refund of money\n")
        else:
            print(f"The Money is not sufficient to have Expresso")

    elif Coffee == "latte":
        if Enough_Money(Latte["Cost"]):
            if Enough_Resources(Water_Quantity, Milk_Quantity, Coffee_Quantity, Latte["Water"], Latte["Milk"],
                                Latte["Coffee"]):
                Water_Quantity -= Latte["Water"]
                Milk_Quantity -= Latte["Milk"]
                Coffee_Quantity -= Latte["Coffee"]
                print("Have your Latte ☕\n\n")
            else:
                print("\nThe Machine dont have resources in enough quantity to make the demanded coffee try some other & also have your Refund of money\n")
        else:
            print(f"The Money is not sufficient to have Latte")

    elif Coffee == "cappuccino":
        if Enough_Money(Cappuccino["Cost"]):
            if Enough_Resources(Water_Quantity, Milk_Quantity, Coffee_Quantity, Cappuccino["Water"], Cappuccino["Milk"],
                                Cappuccino["Coffee"]):
                Water_Quantity -= Cappuccino["Water"]
                Milk_Quantity -= Cappuccino["Milk"]
                Coffee_Quantity -= Cappuccino["Coffee"]
                print("Have your Cappuccino ☕\n\n")
            else:
                print("\nThe Machine dont have resources in enough quantity to make the demanded coffee try some other & also have your Refund of money\n")
        else:
            print(f"The Money is not sufficient to have Cappuccino")
    else:
        print("Enter the valid input")



















































