# Gather input 
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $") 
tip = input("How much tip would you like to give?  10, 12, or 15? ")
split = input("How many people to split the bill? ")  

# Calculate the tip 
tip_total = (float(total_bill) * (int(tip)/100.00)) + float(total_bill)
per_person = round(tip_total / int(split), 2)

# Print out the final amount each person should pay
print(f"Each person should pay: ${per_person:.2f}")
    
