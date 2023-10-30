def Result(Attempts, Random_number):
    Chance = Attempts
    while not (Chance == 0 or False):
        Guess_number = int(input(f"Guess the number you have {Chance} chances left : "))
        if Guess_number == Random_number:
            print(f"You Guessed it right, The number is {Random_number}")
            Chance = False
        elif Guess_number > Random_number:
            print(f"The number is smaller than your guess")
            Chance -= 1
        elif Guess_number < Random_number:
            print(f"The number is larger than your guess")
            Chance -= 1
    if Chance == 0:
        print(f"Sorry, You lost because all your chances are over. & The number was {Random_number}")
























