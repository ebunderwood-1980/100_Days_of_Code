# The Game of Hangman
# Author:  Eric Underwood
# Date:  February 28, 2025

import random
import sys

def print_progress(p):
    return_string = ""
    for item in p:
        return_string += item + " "
    return(return_string)

# TODO:  Randomly choose a word from world_list and assign it to a variable called chosen_word.  Print it.
word_list = ['aardvark', 'babboon', 'camel']
chosen_word = random.choice(word_list)

progress = []
for _ in range(len(chosen_word)):
    progress.append("_")

print(f"Chosen Word:  {chosen_word}")
print(print_progress(progress))

# Game Loop:  Get input, check input against word, print out status.
while True:
    user_guess = input("Please enter your guess:  ").lower()
    if not user_guess.isalpha():
        print("Please enter letters only")
        sys.exit(0)
    print(f"User guessed {user_guess}")

    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            progress[i] = user_guess
            
    if "_" not in progress:
        print("You Win!")
        sys.exit(0)
    else:
        print(print_progress(progress))
