def Enough_Money(Item_Cost):
    Penny = int(input("Enter the amount of Pennys : ")) * 0.01
    Dime = int(input("Enter the amount of Dime : ")) * 0.1
    Nickel = int(input("Enter the amount of Nickel : ")) * 0.05
    Quarter = int(input("Enter the amount of Quarter : ")) * 0.25
    Sum = Penny + Dime + Nickel +Quarter
    if Sum >= Item_Cost:
        print(f"Here is your change ${round((Sum - Item_Cost), 2)}")
        return True


def Enough_Resources(Source_Quantity1, Source_Quantity2, Source_Quantity3, Need_Quantity1, Need_Quantity2, Need_Quantity3):
    if Source_Quantity1 >= Need_Quantity1 and Source_Quantity2 >= Need_Quantity2 and Source_Quantity3 >= Need_Quantity3:
        return True
    else:
        return False






























