# Like list comprehension but lazy
gen = (x ** 2 for x in range(10))
print(gen)   # <generator object>
print(list(gen))

# Memory comparison
import sys
lst = [x for x in range(1000000)]
g = (x for x in range(1000000))
print(f"List: {sys.getsizeof(lst)} bytes")
print(f"Gen:  {sys.getsizeof(g)} bytes")

# With condition
evens = (x for x in range(20) if x % 2 == 0)
print(list(evens))

# As function argument (no extra parens needed)
print(sum(x ** 2 for x in range(10)))
print(any(x > 5 for x in range(10)))
print(all(x < 100 for x in range(10)))
print(max(len(w) for w in ["a", "bb", "ccc"]))

# Chaining
result = sum(x * 2 for x in range(10) if x % 2 == 0)
print(result)

# Nested
matrix = [[1, 2], [3, 4]]
flat_gen = (x for row in matrix for x in row)
print(list(flat_gen))

# Compared to list comp
list_comp = [x ** 2 for x in range(5)]   # eager
gen_exp = (x ** 2 for x in range(5))     # lazy

# When to use
# Generator: large data, single pass
# List: need to iterate multiple times, indexing

# Convert when needed
data = (x for x in range(5))
as_list = list(data)