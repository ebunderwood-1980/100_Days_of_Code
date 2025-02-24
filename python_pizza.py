# Get input
print("Welcome to Python Pizza Deliveries!") 
size = input("What size pizza do you want?  S, M, or L? ").lower()
pepperoni = input("Do you want pepperoni on your pizza?  Y or N? ").lower() 
extra_cheese = input("Do you want extra cheese?  Y or N? ").lower() 

total = 0.00 

# Calculate size and pepperoni
if size == "s":
    total += 15.00  
    if extra_cheese == "y":
        total += 2.00
elif size == "m": 
    total += 20.00
    if extra_cheese == "y":
        total += 3.00 
else: 
    total += 25.00 
    if extra_cheese == "y": 
        total += 3.00

# Calculate cheese 
if extra_cheese == "y": 
    total += 1.00

# Print total
print(f"Total amount due: ${total:.2f}")

