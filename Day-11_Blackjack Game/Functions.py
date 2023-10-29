# TODO 1: Import Zone
import random

# TODO 2: Functions
def Add_item(Items_list):
    """Returns 1 random item from Items_list"""
    return random.choice(Items_list)

def Blackjack_Check(List):
    """Tells whether the items in list have blackjack or not (Return True or False)"""
    if "A" in List and ("10" in List or "K" in List or "Q" in List or "J" in List):
        return True
    else:
        return False



def Dealer_take_a_Card(Player1, Player2, Items_list, Item_Values):
    while not Sum_of_Items(Player2, Item_Values) >= Sum_of_Items(Player1, Item_Values):
        print("Dealer decided to have 1 more card")
        Player2.append(Add_item(Items_list))

def Ask_user_for_a_Card(Player1, Player2, Item_list, Item_values):
    loop = True
    while loop and Sum_of_Items(Player1, Item_values) < 22:
        Extra_Card = input("Enter you want to have 1 more card? (Y or N) : ").lower()
        if Extra_Card == "y":
            Player1.append(Add_item(Item_list))
            print(f"Your cards are {Player1}, and Dealer cards are ['{Player2[0]}', X]")
        else:
            loop = False


def Sum_of_Items(Item_list, Item_values_Dictonary):
    Sum = 0
    for item in Item_list:
        Sum += Item_values_Dictonary[item]
    if "A" in Item_list and Sum <= 11:
        Sum += 10
    else:
        Sum += 0
    return Sum


def Win_or_Lose(Player1, Player2, Item_Values):
    """Tells who Player1 won or lose, (Item_Values is dictonary that contains values of items in Player1&2 list)"""
    if Sum_of_Items(Player1, Item_Values) > 21:
        print(f"Your cards are {Player1} = {Sum_of_Items(Player1, Item_Values)} & Dealer cards are {Player2} = {Sum_of_Items(Player2, Item_Values)}")
        print("YOU LOSE")
    elif Sum_of_Items(Player2, Item_Values) > 21:
        print(f"Your cards are {Player1} = {Sum_of_Items(Player1, Item_Values)} & Dealer cards are {Player2} = {Sum_of_Items(Player2, Item_Values)}")
        print("YOU WON")
    elif Sum_of_Items(Player1, Item_Values) == Sum_of_Items(Player2, Item_Values):
        print(f"Your cards are {Player1} = {Sum_of_Items(Player1, Item_Values)} & Dealer cards are {Player2} = {Sum_of_Items(Player2, Item_Values)}")
        print("DRAW")
    elif Sum_of_Items(Player1, Item_Values) > Sum_of_Items(Player2, Item_Values):
        print(f"Your cards are {Player1} = {Sum_of_Items(Player1, Item_Values)} & Dealer cards are {Player2} = {Sum_of_Items(Player2, Item_Values)}")
        print("YOU WON")
    elif Sum_of_Items(Player2, Item_Values) > Sum_of_Items(Player1, Item_Values):
        print(f"Your cards are {Player1} = {Sum_of_Items(Player1, Item_Values)} & Dealer cards are {Player2} = {Sum_of_Items(Player2, Item_Values)}")
        print("YOU LOSE")































