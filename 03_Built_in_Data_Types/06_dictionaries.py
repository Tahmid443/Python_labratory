# Creating
person = {"name": "Alice", "age": 30}
empty = {}
from_pairs = dict([("a", 1), ("b", 2)])

# Access
print(person["name"])
print(person.get("age"))
print(person.get("city", "Unknown"))  # default

# Modify
person["city"] = "NYC"
person["age"] = 31
print(person)

# Delete
del person["city"]
popped = person.pop("age")
print(person)

# Iterate
for key in person:
    print(key, person[key])
for key, val in person.items():
    print(f"{key}: {val}")
for val in person.values():
    print(val)

# Check
print("name" in person)

# Update
person.update({"email": "a@b.com", "name": "Bob"})
print(person)

# Dict comprehension
squares = {x: x**2 for x in range(5)}
print(squares)

# Nested
users = {
    "alice": {"age": 30, "city": "NYC"},
    "bob":   {"age": 25, "city": "LA"},
}
print(users["alice"]["city"])

# fromkeys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)