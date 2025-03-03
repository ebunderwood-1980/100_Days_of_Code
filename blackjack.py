# Program:  Blackjack Simulator
# Programmer:  Eric Underwood
# Date:  March 2, 2024

import random

logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/        
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
dealer_hidden_card = None

# Function Definitions
def calculate_scores(hand, dealer_card=None): 
    """
    Accepts a list and calculates the value of a given hand, returning either the value of the hand
    or -1 for a bust
    """
    running_count = 0
    for card in hand:
        current_card = cards[card]
        if current_card == "A":
            if running_count + 11 > 21:
                running_count += 1
            else:
                running_count += 11
        else:
            running_count += current_card[0]
    return running_count

# Deal user and computer cards, which will hold the key of the cards key, value pair.
for _ in range(2):
    user_cards.append(random.choice(list(cards.keys())))
computer_cards.append(random.choice(list(cards.keys())))
dealer_hidden_card = random.choice(list(cards.keys()))

# Calculate and print scores
user_score = calculate_scores(user_cards)
computer_score = calculate_scores(computer_cards, dealer_card=dealer_hidden_card) 
print(f"User cards:  {user_cards}, for a score of {user_score}")
print(f"Computer Card: {computer_cards}, for a score of {computer_score}")

# Check to see if the user wants to hit or stay. Continues to deal cards until user hits
# blackjack, busts, or decides to stay
taking_cards = True
while taking_cards:
    user_choice = input("Type 'y' to get another card, type 'n' to pass:  ")
    if user_choice == 'n':
        taking_cards = False
        print(f"Your final hand: {user_cards}")
        computer_cards.append(dealer_hidden_card)
        computer_score = calculate_scores(computer_cards)
        print(f"Computer's final hand:  {computer_cards}") 
        
        if user_score == computer_score:
            print("You Push") 
        elif user_score > computer_score:
            print("You Win") 
        else:
            print("You Loose")
            
    else:                              # User decides to take a hit
        user_cards.append(random.choice(list(cards.keys()))) 
        user_score = calculate_scores(user_cards)
        print(f"User cards:  {user_cards}, for a score of {user_score}")
        
