# Programmer:  Eric Underwood
# Program:  Blackjack
# Date:  March 3, 2025 

import random
from logo import logo
from logo import deck

# Function Definitions
def main():
    # Variable Definitions
    game_over = False 
    player_hand = [] 
    computer_hand = []
    computer_hidden_card = None
    
    # Print out the Blackjack logo
    print(logo)

    # Game loop
    while not game_over:
        # Deal 2 random cards to the user and 1 random card to the computer
        # with another face down random card dealt to the computer as well
        for _ in range(2):
            player_hand.append(random.choice(list(deck.keys()))) 
        computer_hand.append(random.choice(list(deck.keys()))) 
        computer_hidden_card = random.choice(list(deck.keys()))

        # Print out both user and computer hands
        print(f"User Hand: {player_hand}")
        print(f"Computer Hand:  {computer_hand}") 
        print(f"Computer Hidden Card:  {computer_hidden_card}")

        game_over = True



if __name__ == '__main__':
    main()
