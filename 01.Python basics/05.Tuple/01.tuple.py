"""
***********A tuple is a collection which is ordered and unchangeable.***********
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples can also be created without the parentheses:
thistuple = "apple", "banana", "cherry"
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# length of tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Create an empty tuple:
thistuple = ()
print(type(thistuple))

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
