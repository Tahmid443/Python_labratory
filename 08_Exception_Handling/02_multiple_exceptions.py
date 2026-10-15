# Multiple except blocks
def process(data):
    try:
        n = int(data)
        return 100 / n
    except ValueError:
        return "Not a number"
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(process("10"))
print(process("abc"))
print(process("0"))

# Tuple of exceptions
def parse(text):
    try:
        return int(text)
    except (ValueError, TypeError) as e:
        return f"Failed: {e}"

print(parse("42"))
print(parse("abc"))
print(parse(None))

# Order matters! Specific first
def careful():
    try:
        x = int("abc")
    except Exception as e:
        print(f"Generic: {e}")
    except ValueError as e:
        print(f"Specific: {e}")   # unreachable!

# Better
def correct():
    try:
        x = int("abc")
    except ValueError as e:
        print(f"Specific: {e}")
    except Exception as e:
        print(f"Generic: {e}")