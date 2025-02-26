import random 

# User chooses rock, paper, or scissors 
user_choice = int(input("What do you choose?  Type 0 for Rock, 1 for paper, or 2 for scissors "))
if user_choice == 0: 
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user_choice == 1: 
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("\n")  

# Computer chooses rock, paper, scissors 
computer_choice = random.randint(0, 2)
print("Computer chose:\n")
if computer_choice == 0: 
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_choice == 1: 
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""") 
print("\n")

# Determine winner 
if user_choice == 0:
    if computer_choice == 0: 
        print("You tie") 
    elif computer_choice == 1:
        print("You lose") 
    else: 
        print("You win") 
elif user_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 1:
        print("You tie")
    else:
        print("You lose")
else:
    if computer_choice == 0: 
        print("You lose") 
    elif computer_choice == 1:
        print("You win") 
    else:
        print("You tie")  
