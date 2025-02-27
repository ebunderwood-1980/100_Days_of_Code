# By gathering user input on number of numbers, symbols, and letters, create a random strong password

letters = ['a', 'b', 'C', 'D', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Gather user input
print("Welome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password:  "))
num_numbers = int(input("How many numbers would you like in your password:  "))
num_symbols = int(input("How many symbols would you like in your password:  "))



