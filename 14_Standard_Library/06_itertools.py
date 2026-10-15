import itertools as it

# Infinite iterators
print(list(it.islice(it.count(10), 5)))
print(list(it.islice(it.cycle("AB"), 6)))
print(list(it.islice(it.repeat("x", 3), 5)))

# Combinatorics
print(list(it.product("AB", repeat=2)))
print(list(it.permutations("ABC", 2)))
print(list(it.combinations("ABC", 2)))
print(list(it.combinations_with_replacement("AB", 2)))

# Chaining
print(list(it.chain([1, 2], "ab", (True, False))))
print(list(it.chain.from_iterable([[1, 2], [3, 4]])))

# Slicing
print(list(it.islice(range(100), 5)))
print(list(it.islice(range(100), 10, 20, 2)))

# Grouping
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
for k, g in it.groupby(data, key=lambda x: x[0]):
    print(k, list(g))

# Accumulate
print(list(it.accumulate([1, 2, 3, 4])))
print(list(it.accumulate([1, 2, 3, 4], lambda a, b: a * b)))

# Filter
print(list(it.compress("ABCD", [1, 0, 1, 0])))
print(list(it.dropwhile(lambda x: x < 3, range(10))))
print(list(it.takewhile(lambda x: x < 3, range(10))))

# Zipping
print(list(it.zip_longest([1, 2, 3], "ab", fillvalue="?")))

# Pairwise (3.10+)
print(list(it.pairwise([1, 2, 3, 4])))

# Grouping into chunks
def chunks(lst, n):
    it_obj = iter(lst)
    while chunk := list(it.islice(it_obj, n)):
        yield chunk
print(list(chunks(range(10), 3)))