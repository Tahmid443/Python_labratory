s = "  Hello, World!  "

# Cleaning
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.strip(" !"))

# Case
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.capitalize())

# Search
print(s.find("World"))
print(s.find("xyz"))       # -1
print(s.index("World"))
# s.index("xyz")           # ValueError
print(s.count("l"))
print(s.startswith("  He"))
print(s.endswith("!  "))

# Modify
print(s.replace("World", "Python"))
print(s.replace("l", "L", 2))   # max 2 replacements

# Split / join
csv = "a,b,c"
print(csv.split(","))
print(" ".join(["a", "b", "c"]))

print("line1\nline2".splitlines())

# Checks
print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("   ".isspace())
print("Hello".istitle())
print("HELLO".isupper())
print("hello".islower())

# Padding
print("5".zfill(3))
print("hi".center(10, "*"))
print("hi".ljust(10, "."))
print("hi".rjust(10, "."))

# Casefold (better than lower for comparisons)
print("STRASSE".casefold() == "straße".casefold())

# Encode/decode
b = "hello".encode("utf-8")
print(b)
print(b.decode("utf-8"))