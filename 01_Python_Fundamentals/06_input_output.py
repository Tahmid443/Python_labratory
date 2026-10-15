# Basic output
print("Hello", "World", sep=", ", end="!\n")

# Formatted output
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")

# Input (returns string)
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Input with conversion
# age = int(input("Enter your age: "))
# print(f"Next year you'll be {age + 1}")

# Reading multiple values
# a, b = map(int, input("Enter two numbers: ").split())
# print(f"Sum: {a + b}")

# Simulated input for demo
import io, sys
sys.stdin = io.StringIO("Alice\n30\n")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")