# Program Name:  silent_auction.py
# Programmer:  Eric Underwood
# Date:  March 1, 2025

import silent_art

print(silent_art.logo)

auction_finished = False
bidders_dict = {} 
highest_bidder = ""

while not auction_finished:
    # Gather input from users
    user_name = input("What is your name?:  ") 
    bid = int(input("What is your bid?: $")) 
    more_bidders = input("Are there any other bidders?  Type 'yes' or 'no'.:  ").lower() 

    # Add bidders and respective bids to bidders_dict
    bidders_dict[user_name] = bid

    # Check to see if there are any more bidders, if so, scroll down 
    if more_bidders == "yes":
        print("\n"*100) 
    else:
        auction_finished = True 

# Loop through the bidders_dict and find the highes bid
    






