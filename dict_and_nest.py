# Dictionaries and Nesting
# Key, Value pairs, searchable by the key.

dict = {
    "key": "value", 
    "key2": "value2",
    } 

print(dict["key"])

dict["new"] = "stuff" 

# Wipes out the entire dictionary
# dict = {} 

# Printing out keys and values of a dictionary
for key in dict:
    print(key)        # Prints out just the key.
    print(dict[key])  # Prints out the value at dict[key]

# Nesting:  Putting lists and dictionaries inside of one another.
# {
#     Key: [List],
#     Key2: {Dict},
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"],
}

# Print "Lille" from the travel log
print(f"Did I print Lille:  {travel_log["France"][1]}")

# Nested list
nested_list = ["A", "B", ["C", "D"]]
print(f"Did I print 'D':  {nested_list[2][1]}") 

# Accessing values from a nested dictionary
dict2 = {
    "France": {
        "Cities_Visited": ["Paris", "Lille", "Dijon"],
        "Total_Visits" : 12,
    },
    "Germany": {
        "Cities_Visited": ["Stuttgart", "Berlin"],
        "Total_Visits": 5
    },
}
print(f"Did I visit 'Stuttgart':  {dict2["Germany"]["Cities_Visited"][0]}")
