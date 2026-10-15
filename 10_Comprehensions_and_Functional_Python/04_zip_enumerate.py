# zip - combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Uneven lengths - stops at shortest
print(list(zip([1, 2, 3], ["a", "b"])))

# zip_longest
from itertools import zip_longest
print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="?")))

# Unzip
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums, letters)

# Create dict from two lists
mapping = dict(zip(names, ages))
print(mapping)

# enumerate
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Custom start
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

# Convert to list
print(list(enumerate(fruits)))

# Unpacking
indexed = list(enumerate(fruits))
for (i, item) in indexed:
    print(i, item)

# Multiple zip
for i, (name, age) in enumerate(zip(names, ages)):
    print(f"{i}: {name} ({age})")