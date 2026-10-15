# map
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)

# Named function
def square(x):
    return x ** 2

print(list(map(square, nums)))

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# None as filter (removes falsy)
mixed = [0, 1, "", "a", None, [], [1]]
truthy = list(filter(None, mixed))
print(truthy)

# Combined
result = list(map(square, filter(lambda x: x % 2 == 0, nums)))
print(result)

# Equivalent comprehension
result2 = [x ** 2 for x in nums if x % 2 == 0]
print(result2)

# reduce
from functools import reduce
product = reduce(lambda a, b: a * b, nums)
print(product)

# map returns iterator (lazy)
m = map(str, nums)
print(m)   # <map object>
print(list(m))

# When to use which?
# map/filter: when you have existing functions
# comprehensions: when you have expressions