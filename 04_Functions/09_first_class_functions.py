# Functions are objects
def greet(name):
    return f"Hello, {name}"

say_hi = greet
print(say_hi("Alice"))

# Pass as argument
def apply(func, value):
    return func(value)

print(apply(greet, "Bob"))
print(apply(str.upper, "hello"))

# Return function
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))

# Store in data structures
ops = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
}
print(ops["add"](3, 4))

# Higher-order functions
def compose(f, g):
    return lambda x: f(g(x))

add1 = lambda x: x + 1
double = lambda x: x * 2
combined = compose(add1, double)
print(combined(5))  # (5*2)+1 = 11

# Built-in higher-order
nums = [1, 2, 3, 4]
print(list(map(str, nums)))
print(list(filter(lambda x: x > 2, nums)))