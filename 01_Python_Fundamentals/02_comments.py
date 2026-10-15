# This is a single-line comment

# Comments are ignored by the interpreter
# They help explain what the code does

"""
This is a multi-line string
Often used as a docstring or block comment
"""

def add(a, b):
    """Return the sum of two numbers."""  # Docstring
    return a + b

# Good comments explain WHY, not WHAT
# Bad:  x = x + 1  # increment x
# Good: x = x + 1  # adjust for 1-based indexing

if __name__ == "__main__":
    print(add(2, 3))