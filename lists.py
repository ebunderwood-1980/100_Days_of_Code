import random

states_of_america = ["new mexico", "texas", "arizona"]

# Lists store related data in the order that the data is entered. 
# Can use negative indexes to access end of list (-1 etc.) 
# Can amend data in list 
states_of_america[1] = "texass" 

states_of_america.append("florida") # adds "florida" to the end of the states_of_america list 

# Extend is like append, but instead of adding a single item, you are adding an entire list
states_of_america.extend(["connecticut", "new york", "delaware"])

# Banker Roulette:  Pick out random friend to pay the bill. 
friends = ["Eric", "Jacqui", "Aristotle", "Nyx"]
print(f"The unfortunate person is: {random.choice(friends)}")

 
# Nested lists 
evens = [2, 4, 6, 8] 
odds = [1, 3, 5, 7, 9] 
numbers = [evens, odds]
print(numbers) 
