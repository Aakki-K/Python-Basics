# TODO 1: Import Zone
from art import logo
from Containers import Cards, Card_Value_Dictonary
from Functions import Add_item, Blackjack_Check, Win_or_Lose, Ask_user_for_a_Card, Dealer_take_a_Card, Sum_of_Items

# TODO 2: Print logo
print(logo)

# TODO 3: creating list for Player1 & Player2, & appending 2 random cards
Player1_Cards = [] # Player
Player2_Cards = [] # Dealer

# Adding 2 Cards to Dealer
Player2_Cards.append(Add_item(Cards))
Player2_Cards.append(Add_item(Cards))

# Adding 2 Cards to Player
Player1_Cards.append(Add_item(Cards))
Player1_Cards.append(Add_item(Cards))

# TODO 4: Check for Blackjack

# # Test
# Player1_Cards = ["A", "3"]
# Player2_Cards = ["A", "K"]

# Both Blackjack
if Blackjack_Check(Player1_Cards) and Blackjack_Check(Player2_Cards):
    print("Ohh, Blackjack")
    Win_or_Lose(Player1_Cards, Player2_Cards, Card_Value_Dictonary)
elif Blackjack_Check(Player1_Cards):
    print("Ohh, Blackjack")
    Win_or_Lose(Player1_Cards, Player2_Cards, Card_Value_Dictonary)
elif Blackjack_Check(Player2_Cards):
    print("Ohh, Blackjack")
    Win_or_Lose(Player1_Cards, Player2_Cards, Card_Value_Dictonary)
else: # if not blackjack
    print(f"Your cards are {Player1_Cards}, and Dealer cards are ['{Player2_Cards[0]}', X]")
    Ask_user_for_a_Card(Player1_Cards, Player2_Cards, Cards, Card_Value_Dictonary)
    if Sum_of_Items(Player1_Cards, Card_Value_Dictonary) > 21:
        Win_or_Lose(Player1_Cards, Player2_Cards, Card_Value_Dictonary)
    else: # If not over 21
        Dealer_take_a_Card(Player1_Cards, Player2_Cards, Cards, Card_Value_Dictonary)
        Win_or_Lose(Player1_Cards, Player2_Cards, Card_Value_Dictonary)

























