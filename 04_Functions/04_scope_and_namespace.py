# Global scope
x = 10

def read_global():
    print(x)   # reads global

def modify_global():
    global x
    x = 20

read_global()
modify_global()
print(x)

# Local scope
def local_demo():
    y = 5
    print(y)

local_demo()
# print(y)  # NameError

# Enclosing (nonlocal)
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter = outer()
print(counter(), counter(), counter())

# LEGB rule: Local -> Enclosing -> Global -> Built-in
name = "global"

def show():
    name = "local"
    print(name)

show()
print(name)

# Built-in
def print_len(lst):
    print(len(lst))  # len is built-in

print_len([1, 2, 3])

# Avoid globals - pass as arguments
def better_add(a, b, c=0):
    return a + b + c