# Positional
def sub(a, b):
    return a - b

print(sub(10, 3))
print(sub(b=10, a=3))    # keyword
# print(sub(a=10, 3))    # SyntaxError

# Mix (positional before keyword)
def power(base, exp):
    return base ** exp

print(power(2, 3))
print(power(base=2, exp=3))

# Positional-only (Python 3.8+)
def f(a, b, /, c):
    return a + b + c

print(f(1, 2, 3))
print(f(1, 2, c=3))
# print(f(a=1, b=2, c=3))  # Error

# Keyword-only (after *)
def g(a, *, b, c):
    return a + b + c

print(g(1, b=2, c=3))
# print(g(1, 2, 3))  # Error

# All combined
def h(a, b, /, c, *, d):
    return a + b + c + d

print(h(1, 2, 3, d=4))