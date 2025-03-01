# The Game of Hangman
# Author:  Eric Underwood
# Date:  February 28, 2025

import random

def print_progress(p):
    return_string = ""
    for item in p:
        return_string += item + " "
    return(return_string) 


stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] 

word_list = ['aardvark', 'babboon', 'camel']
chosen_word = random.choice(word_list)

progress = []
for _ in range(len(chosen_word)):
    progress.append("_")

print(f"Chosen Word:  {chosen_word}")
print(print_progress(progress))

# Game Loop:  Get input, check input against word, print out status.
done = False
wrong_guesses = 0
print(stages[wrong_guesses])
while not done and wrong_guesses <= 5:
    user_guess = input("Please enter your guess:  ").lower()

    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            progress[i] = user_guess
    if user_guess not in chosen_word:
        print(f"{user_guess} is not in the secret word")
        wrong_guesses += 1
        print(stages[wrong_guesses])
            
    if "_" not in progress:
        print(f"You Win!  You guessed '{chosen_word.upper()}'")
        done = True
    else:
        print(print_progress(progress)+"\n")
        if wrong_guesses > 5:
            print("No more guesses.  You lose!")
