# *args - variable positional
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))

# **kwargs - variable keyword
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

print_info(name="Alice", age=30, city="NYC")

# Combined
def full(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

full(1, 2, 3, 4, x=10, y=20)

# Unpacking at call site
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add3(*nums))

opts = {"a": 1, "b": 2, "c": 3}
print(add3(**opts))

# Flexible function
def flexible(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword:    {kwargs}")

flexible(1, 2, x=3, y=4)