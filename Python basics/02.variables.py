"""
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

1.A variable name must start with a letter or the underscore character
2.A variable name cannot start with a number
3.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4.Variable names are case-sensitive (age, Age and AGE are three different variables)
5.A variable name cannot be any of the Python keywords.
"""
fruit = "banana"
weight = 40
height = 5.6
print(fruit," ",weight," ",height)

# multiple variables
x,y,z = "apple","orange","mango"
print(x)
print(y)
print(z)
# we can also unpack from any collection
marks = [90,89,85]
a,b,c = marks
print(a)
print(b)
print(c)

# global and local
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

x = "awesome" #its global
def myfunc():
    print("Python is " + x)
myfunc()

# using global keyword

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
