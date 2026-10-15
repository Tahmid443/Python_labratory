name = "Alice"
age = 30

# % formatting (old)
print("Name: %s, Age: %d" % (name, age))
print("Pi: %.2f" % 3.14159)

# str.format
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Alignment
print("{:<10}|".format("left"))
print("{:>10}|".format("right"))
print("{:^10}|".format("center"))

# Numbers
print("{:.2f}".format(3.14159))
print("{:,}".format(1000000))
print("{:%}".format(0.25))
print("{:b}".format(255))   # binary
print("{:o}".format(255))   # octal
print("{:x}".format(255))   # hex

# f-strings (recommended)
print(f"Name: {name}, Age: {age}")
print(f"Next year: {age + 1}")
print(f"Pi: {3.14159:.2f}")
print(f"{name=}, {age=}")   # debug (3.8+)

# Expression
print(f"Upper: {name.upper()}")
print(f"Sum: {1 + 2 + 3}")

# Nested
width = 10
print(f"{'hi':>{width}}")