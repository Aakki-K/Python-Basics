# TODO 1: Import Zone
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 2: Code
# creating object
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Code

Is_Loop = True #Keeping loop
while Is_Loop:
    User_Choice = input(f"Which coffee you wanna have {menu.get_items()} ? : ") # Taking choice from user
    if User_Choice == "report":
        print(coffee_maker.report()) #Displaying Report of resources available
        print(money_machine.report()) #Displaying Report of profit
    elif User_Choice == "off":
        Is_Loop = False
    else:
        menu_item = menu.find_drink(User_Choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)















