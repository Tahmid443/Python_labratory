# Basic for loop
for i in range(5):
    print(i, end=" ")
print()

# With start/stop/step
for i in range(1, 10, 2):
    print(i, end=" ")
print()

# Reverse
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# Iterate list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# With index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Iterate dict
person = {"name": "Alice", "age": 30}
for key in person:
    print(key, person[key])
for key, val in person.items():
    print(f"{key} = {val}")

# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}*{j}={i*j}", end="\t")
    print()