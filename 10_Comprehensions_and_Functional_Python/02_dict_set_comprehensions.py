# Dict comprehension
squares = {x: x**2 for x in range(5)}
print(squares)

# Transform dict
prices = {"apple": 1.0, "banana": 0.5}
discounted = {k: v * 0.9 for k, v in prices.items()}
print(discounted)

# Filter dict
cheap = {k: v for k, v in prices.items() if v < 1}
print(cheap)

# Swap keys and values
swapped = {v: k for k, v in prices.items()}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
mapping = {k: v for k, v in zip(keys, values)}

# Conditional value
labels = {x: "even" if x % 2 == 0 else "odd" for x in range(5)}

# Set comprehension
evens = {x for x in range(20) if x % 2 == 0}
print(evens)

unique_lengths = {len(w) for w in ["a", "bb", "ccc", "dd"]}
print(unique_lengths)

# From string
unique_chars = {c for c in "hello world" if c != " "}
print(unique_chars)

# Nested
matrix = [[1, 2], [3, 4]]
flat_set = {x for row in matrix for x in row}
print(flat_set)

# Word lengths
text = "the quick brown fox"
word_lengths = {word: len(word) for word in text.split()}
print(word_lengths)