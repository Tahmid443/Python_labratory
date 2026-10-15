# Variables are dynamically typed
name = "Alice"
age = 30
height = 5.6
is_student = False

print(f"{name} is {age} years old, {height} ft tall")

# Multiple assignment
x, y, z = 1, 2, 3
print(x, y, z)

# Same value
a = b = c = 0
print(a, b, c)

# Swap
x, y = y, x
print(f"x={x}, y={y}")

# Naming conventions (PEP 8)
# snake_case for variables
first_name = "John"
# UPPER_CASE for constants
MAX_SIZE = 100
# Avoid single letters except for counters