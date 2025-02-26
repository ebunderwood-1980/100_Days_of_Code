import random
import my_module

# Generate a random integer between a and b (inclusive)
for _ in range(10):
    rand = random.randint(0, 3)
    print(rand)
    
# Get my_favorite_number data member from file my_module.py
print(my_module.my_favorite_number)

# Generate a random floating point number between 0 and 1. 1 non inclusive
for _ in range(5):
    random_number_0_to_1 = random.random()
    print(random_number_0_to_1)

# Generate a random floating point number between a and b, inclusive
for _ in range(5):
    print(f"Random.Unform(0,10) = {random.uniform(0,10)}")


# Heads or tails program using random
for _ in range(5):
    random_number = random.randint(0,1)
    if random_number == 1:
        print("heads!")
    else:
        print("tails!")
    
