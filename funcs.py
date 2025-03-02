# Functions

def my_function():
    print("Hello")

my_function()

# While loop
x = 5
while x > 0:
    print(x)
    x -= 1

# Create function called Greet(), write 3 print statements inside of greet, then call greet.
def greet(something): 
    """This function says hello"""   #This is a docstring.
    print(f"Hello, {something}")
    print("This is the greet function")
    print("Good bye") 

greet("Eric")


def keyword_arguments(first, second, third): 
    print(first) 
    print(second) 
    print(third)

keyword_arguments(third = "third", first = "first", second = "second")  

# Take two inputs returns title case single string
def format_name(f_name, l_name):
    return(f"{f_name.title()} {l_name.title()}")

print(f"Format Name:  {format_name("eric", "underwood")}")



