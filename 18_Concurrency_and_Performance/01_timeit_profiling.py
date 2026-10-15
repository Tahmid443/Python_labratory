import timeit

# timeit basics
t = timeit.timeit("sum(range(100))", number=10000)
print(f"Sum: {t:.4f}s")

# With setup
t = timeit.timeit(
    "sorted(data)",
    setup="import random; data = [random.random() for _ in range(1000)]",
    number=100,
)
print(f"Sort: {t:.4f}s")

# Compare implementations
def list_comp():
    return [x ** 2 for x in range(100)]

def map_lambda():
    return list(map(lambda x: x ** 2, range(100)))

t1 = timeit.timeit(list_comp, number=10000)
t2 = timeit.timeit(map_lambda, number=10000)
print(f"List comp: {t1:.4f}s")
print(f"Map lambda: {t2:.4f}s")

# repeat (get min - more reliable)
times = timeit.repeat("sum(range(100))", number=1000, repeat=5)
print(f"Min: {min(times):.6f}, Mean: {sum(times)/len(times):.6f}")

# %timeit in IPython/Jupyter:
# %timeit sum(range(100))
# %%timeit  (whole cell)