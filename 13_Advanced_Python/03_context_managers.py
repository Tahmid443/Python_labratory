# Context manager protocol: __enter__, __exit__

# with open()
with open("test.txt", "w") as f:
    f.write("hello")

with open("test.txt") as f:
    print(f.read())

# Without with
f = open("test.txt")
try:
    print(f.read())
finally:
    f.close()

# Custom
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False   # don't suppress exceptions

with Timer() as t:
    sum(range(1000000))

# Exception handling in __exit__
class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.exceptions)

with Suppress(ValueError):
    int("abc")
    print("Never reached")
print("Continued")

# Multiple managers
with open("a.txt", "w") as a, open("b.txt", "w") as b:
    a.write("A")
    b.write("B")

import os
for fn in ["test.txt", "a.txt", "b.txt"]:
    if os.path.exists(fn):
        os.remove(fn)