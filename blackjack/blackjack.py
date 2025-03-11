from constants import DECK
from constants import LOGO
import random


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

if computer_hand[0] == 'A':
    print("Ace showing, checking Dealer's Hole Card...") 
    if DECK[computer_hand[1]][0] == 10: 
        print("Dealer hits Blackjack!")
        game_over = True
    else:
        print("No dice, lucky break")
if computer_hand[0] in ['K', 'Q', 'J', '10']:
    print("Face card showing, checking Dealer's Hole Card...")
    if computer_hand[1] == 'A':
        print("Dealer hits Blackjack!")
        game_over = True
    else:
        print("No dice, lucky break")

while user_turn:
    take_hit = input("Type 'y' to get another card, type 'n' to pass:  ")

    
