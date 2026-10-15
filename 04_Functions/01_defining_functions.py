# Basic function
def greet():
    print("Hello!")

greet()

# With parameter
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")

# With return
def add(a, b):
    return a + b

print(add(2, 3))

# Multiple returns (tuple)
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([1, 5, 3])
print(lo, hi)

# Docstrings
def area(radius):
    """Return the area of a circle given radius."""
    import math
    return math.pi * radius ** 2

print(area.__doc__)
print(area(5))

# Nested functions
def outer():
    def inner():
        return "inner"
    return inner()

print(outer())

# Function as variable
f = add
print(f(1, 2))