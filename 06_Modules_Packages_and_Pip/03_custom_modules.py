"""
This file demonstrates creating a custom module.
In practice, you would save utility functions in a separate file
(e.g., myutils.py) and import them.
"""

# --- Save this as myutils.py ---
MYUTILS_SOURCE = '''
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

class Calculator:
    def __init__(self):
        self.history = []
    def compute(self, expr):
        result = eval(expr)
        self.history.append((expr, result))
        return result
'''
# --- End ---

# Simulate importing
import types
myutils = types.ModuleType("myutils")
exec(MYUTILS_SOURCE, myutils.__dict__)

print(myutils.add(2, 3))
print(myutils.PI)

calc = myutils.Calculator()
print(calc.compute("2 + 3 * 4"))
print(calc.history)

# When in real file:
# import myutils
# from myutils import add, PI