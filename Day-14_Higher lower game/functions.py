# TODO 1: Function

def Random_Item(Item_list):
    import random
    return random.choice(Item_list)

def Result(User_Choice, Other_Option, Option_value_dictonary):
    if Option_value_dictonary[User_Choice] > Option_value_dictonary[Other_Option]:
        return True
    else:
        return False











