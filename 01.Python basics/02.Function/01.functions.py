# A function is a block of code which only runs when it is called.
# In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def my_function():
    print("Hello from a function")
my_function()#way to call a function/ we can call it multiple time

"""
Function names follow the same rules as variable names in Python:

1.A function name must start with a letter or underscore
2.A function name can only contain letters, numbers, and underscores
3.Function names are case-sensitive (myFunction and myfunction are different)
"""


# Return Values
# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:
def get_greeting():
    return "Hello from a function"


message = get_greeting()
print(message)
# If a function doesn't have a return statement, it returns None by default.


# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
    pass
