# Arithmetic
a, b = 10, 3
print(f"Add: {a + b}")
print(f"Sub: {a - b}")
print(f"Mul: {a * b}")
print(f"Div: {a / b}")
print(f"Floor Div: {a // b}")
print(f"Mod: {a % b}")
print(f"Pow: {a ** b}")

# Comparison
print(5 > 3, 5 < 3, 5 == 5, 5 != 3, 5 >= 5, 5 <= 3)

# Logical
print(True and False)
print(True or False)
print(not True)

# Assignment
x = 5
x += 3   # x = x + 3
x -= 1
x *= 2
x //= 3
x **= 2
print(x)

# Identity (is)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)   # True
print(a is c)   # False

# Membership
print(2 in [1, 2, 3])
print("a" not in "hello")

# Bitwise
print(5 & 3)    # 1
print(5 | 3)    # 7
print(5 ^ 3)    # 6
print(~5)       # -6
print(5 << 1)   # 10
print(5 >> 1)   # 2