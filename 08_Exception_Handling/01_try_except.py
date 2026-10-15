# Basic
try:
    x = int("abc")
except ValueError:
    print("Could not convert!")

# Access exception
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Generic
try:
    d = {}
    print(d["missing"])
except Exception as e:
    print(f"Caught: {type(e).__name__}: {e}")

# Function example
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_div(10, 2))
print(safe_div(10, 0))

# Nested try
try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner handler")
        raise
except Exception as e:
    print(f"Outer: {e}")