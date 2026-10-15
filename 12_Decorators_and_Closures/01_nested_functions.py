def outer():
    print("Outer start")

    def inner():
        print("Inner")

    inner()
    inner()
    print("Outer end")

outer()

# Inner uses outer variable
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3), add10(3))

# Multiple levels
def a():
    def b():
        def c():
            return "deep"
        return c()
    return b()

print(a())

# Return multiple functions
def make_ops():
    def add(a, b): return a + b
    def sub(a, b): return a - b
    def mul(a, b): return a * b
    return add, sub, mul

add, sub, mul = make_ops()
print(add(2, 3), sub(5, 2), mul(4, 3))