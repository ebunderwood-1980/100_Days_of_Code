# Looping through a list.
your_list = ["Eric", "Jacqui", "Aritotle", "Nyx"]
for item in your_list:
    print(item)

# Sum of lists
total_exam_score = sum([1,2,3,4,5])
print(total_exam_score)

# Implementing the sum() function using for loops.
numbers = [1, 2, 3, 4, 5, 10]
total = 0
for number in numbers:
    total += number
print(f"Sum Using For Loop:  {total}")

# Implement the max() functionality using a for loop.
max = float('-inf')
numbers = [180, 123, 165, 173, 189, 169, 146]
for number in numbers:
    if number > max:
        max = number
print(f"Max number is: {max}")

# Using range() function in for loop to add up numbers from 1 to 100
sum = 0
for number in range(1, 101):  # Range does not include upper bound.
    sum += number
print(f"Sum is {sum}")


# Fizz buzz from 1 to 100.
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
