# Implicit conversion
result = 5 + 3.14   # int + float => float
print(result, type(result))

# Explicit conversion
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(num_int, num_float)

# To string
num = 100
print("Number: " + str(num))

# Boolean conversion
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool(None))    # False
print(bool(1))       # True
print(bool("a"))     # True

# Errors
try:
    int("hello")
except ValueError as e:
    print(f"Error: {e}")

# Rounding
print(round(3.14159, 2))
print(int(3.99))     # 3 (truncates)