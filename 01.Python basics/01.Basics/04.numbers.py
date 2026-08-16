"""
There are three numeric types in Python:

int
float
complex
"""
a = 1
b = 1.4
c = 2j

# int
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# complex
x = 35e3
y = 12e4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# type conversion
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
