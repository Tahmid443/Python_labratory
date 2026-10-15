# List comprehension
squares = [x**2 for x in range(10)]
print(squares)

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)

# Flatten
flat = [x for row in matrix for x in row]
print(flat)

# Set comprehension
unique_lengths = {len(w) for w in ["a", "bb", "ccc", "dd"]}
print(unique_lengths)

# Dict comprehension
square_map = {x: x**2 for x in range(5)}
print(square_map)

# Generator expression (lazy)
gen = (x**2 for x in range(5))
print(sum(gen))

# When NOT to use
# Avoid complex nested comprehensions - use loops instead