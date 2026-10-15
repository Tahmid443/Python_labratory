# Creating strings
s = "Hello, World"
print(s)

# Indexing and slicing
print(s[0])       # H
print(s[-1])      # d
print(s[0:5])     # Hello
print(s[::2])     # Hlo ol
print(s[::-1])    # dlroW ,olleH

# Immutability
# s[0] = "h"  # TypeError

# Concatenation & repetition
print("Hello" + " " + "World")
print("=" * 20)

# Membership
print("World" in s)
print("Python" not in s)

# Iteration
for ch in "abc":
    print(ch, end=" ")
print()

# Raw & f-strings
name = "Alice"
print(f"Hello, {name}!")

# Common escapes
print("Tab\there")
print("Line\nBreak")