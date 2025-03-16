from constants import DECK


def check_blackjack(hand):
    if hand[0] == "A":
        print("Ace showing, checking Dealer's Hole Card...")
        if DECK[hand[1]][0] == 10:
            print("Dealer hits Blackjack!")
            return True
        else:
            print("No dice, lucky break")
            return False
    elif hand[0] in ["K", "Q", "J", "10"]:
        print("Face card showing, checking Dealer's Hole Card...")
        if hand[1] == "A":
            print("Dealer hits Blackjack!")
            return True
        else:
            print("No dice, lucky break")
            return False
