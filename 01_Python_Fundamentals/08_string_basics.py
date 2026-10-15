# Creating strings
s1 = "Hello"
s2 = 'World'
s3 = """Multi
line"""
s4 = '''Also
multi
line'''

# Concatenation
greeting = s1 + ", " + s2
print(greeting)

# Repetition
print("ab" * 3)

# Length
print(len(s1))

# Indexing (0-based)
print(s1[0], s1[-1])

# Slicing
print(s1[1:4])
print(s1[:3])
print(s1[2:])
print(s1[::-1])  # reverse

# Iteration
for ch in s1:
    print(ch, end=" ")
print()

# Immutability
# s1[0] = "J"  # TypeError

# Escape sequences
print("Tab:\tEnd")
print("Newline:\nEnd")
print("Quote: \"Hi\"")
print("Backslash: \\")

# Raw strings
print(r"C:\Users\name")