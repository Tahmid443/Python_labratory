# Basic default
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))

# Default evaluated once!
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(bad_append(1))   # [1]
print(bad_append(2))   # [1, 2] - BUG!

# Correct way
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good_append(1))
print(good_append(2))

# Mutable defaults
def add_student(name, roster=None):
    if roster is None:
        roster = []
    roster.append(name)
    return roster

# Default after non-default
def f(a, b=2, c=3):
    return a + b + c

print(f(1))
print(f(1, 5))
print(f(1, 5, 10))