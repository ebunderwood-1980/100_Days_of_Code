from constants import DECK
from constants import LOGO
import random
from functions import check_blackjack
import sys


# Variables
user_hand = []
computer_hand = []
game_over = False
user_turn = True

print(LOGO)

for _ in range(2):
    user_hand.append(random.choice(list(DECK.keys())))
    computer_hand.append(random.choice(list(DECK.keys())))

print(f"User hand:  {user_hand}")
print(f"Computer hand:  {computer_hand}")

# Check to see if Dealer hit Blackjack
if check_blackjack(computer_hand):
    print("Game Over")
    sys.exit

while user_turn:
    take_hit = input("Type 'y' to get another card, type 'n' to pass:  ")
    pass
