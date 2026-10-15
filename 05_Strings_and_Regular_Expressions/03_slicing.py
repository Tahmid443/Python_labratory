s = "Python Programming"

# Basic
print(s[0:6])       # Python
print(s[7:])        # Programming
print(s[:6])        # Python
print(s[:])         # full copy

# Negative
print(s[-11:])      # Programming
print(s[:-12])      # Python

# Step
print(s[::2])       # every 2nd char
print(s[::-1])      # reverse

# Reverse words (not chars)
words = s.split()
print(" ".join(words[::-1]))

# Slice assignment (list only)
lst = [1, 2, 3, 4, 5]
lst[1:4] = [10, 20, 30]
print(lst)

lst[::2] = [0, 0, 0]
print(lst)

# Delete via slice
del lst[1:3]
print(lst)

# Copy list via slice
original = [1, 2, 3]
copy = original[:]
copy.append(4)
print(original, copy)

# Out of bounds is OK
print(s[100:200])   # empty string

# Common idiom: safe copy
data = [1, 2, 3]
backup = data[:]