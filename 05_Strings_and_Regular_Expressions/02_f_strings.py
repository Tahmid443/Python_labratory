name = "Alice"
age = 30
pi = 3.14159

# Basic
print(f"Hello, {name}!")

# Expressions
print(f"{age + 1} years old next year")
print(f"{name.upper()}")
print(f"{'even' if age % 2 == 0 else 'odd'}")

# Format spec
print(f"{pi:.3f}")
print(f"{age:05d}")
print(f"{1000000:,}")

# Nested f-string
print(f"{f'{name}':>10}")

# Dict access
person = {"name": "Bob", "age": 25}
print(f"{person['name']} is {person['age']}")

# Attribute access
class P:
    def __init__(self):
        self.name = "Obj"
p = P()
print(f"{p.name}")

# Debug
x = 42
print(f"{x=}")
print(f"{x * 2 = }")

# Multiline
msg = (
    f"Name: {name}\n"
    f"Age:  {age}\n"
    f"Pi:   {pi:.2f}"
)
print(msg)

# Escape
print(f"{{literal braces}}")