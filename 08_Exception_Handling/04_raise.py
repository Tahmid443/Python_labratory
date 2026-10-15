# Raise existing
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")

# Re-raise
def process(data):
    try:
        return int(data)
    except ValueError:
        print("Logging error...")
        raise

try:
    process("abc")
except ValueError:
    print("Handled at top level")

# Raise from (chain)
def outer():
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("Processing failed") from e

try:
    outer()
except RuntimeError as e:
    print(f"{e}")
    print(f"Caused by: {e.__cause__}")

# assert-like pattern
def check_positive(x):
    if x <= 0:
        raise ValueError(f"Expected positive, got {x}")
    return x