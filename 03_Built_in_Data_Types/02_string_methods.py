s = "  Hello, World!  "

# Case
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

# Trim
print(repr(s.strip()))
print(repr(s.lstrip()))
print(repr(s.rstrip()))

# Search
print(s.find("World"))
print(s.rfind("l"))
print(s.count("l"))
print(s.startswith("  He"))
print(s.endswith("!  "))

# Replace
print(s.replace("World", "Python"))

# Split & join
text = "a,b,c,d"
parts = text.split(",")
print(parts)
print("-".join(parts))

# Check
print("hello".isalpha())
print("123".isdigit())
print(" ".isspace())
print("abc123".isalnum())

# Format
print("{} is {}".format("Alice", 30))
print("{name} is {age}".format(name="Bob", age=25))

# Padding
print("5".zfill(3))
print("hi".center(10, "*"))
print("hi".ljust(10, "."))
print("hi".rjust(10, "."))