# Program:  Blackjack Simulator
# Programmer:  Eric Underwood
# Date:  March 2, 2024

import random

logo = '''

    
'''

cards = {
    "A": [1, 11],
    "K": [10],
    "Q": [10],
    "J": [10],
    "10": [10],
    "9": [9],
    "8": [8],
    "7": [7],
    "6": [6],
    "5": [5],
    "4": [4],
    "3": [3],
    "2": [2],
}

print(logo) 

# Variables
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0
game_over = False

# Function Definitions
def calculate_scores(hand): 
    """
    Accepts a list and calculates the value of a given hand, returning either the value of the hand
    or -1 for a bust
    """
    pass

# Deal user and computer cards, which will hold the key of the cards key, value pair.
for _ in range(2):
    user_cards.append(random.choice(list(cards.keys())))
computer_cards.append(random.choice(list(cards.keys())))

# Calculate scores

print(f"User cards:  {user_cards}")
print(f"Computer Card: {computer_cards}")

