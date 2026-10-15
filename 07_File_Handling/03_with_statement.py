# Without with (must close manually)
f = open("data.txt", "w")
try:
    f.write("Hello")
finally:
    f.close()

# With with (auto-closes, even on exception)
with open("data.txt", "w") as f:
    f.write("Hello")

# Multiple files
with open("in.txt", "w") as f:
    f.write("source")

with open("in.txt") as fin, open("out.txt", "w") as fout:
    for line in fin:
        fout.write(line.upper())

# Custom context manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    def __exit__(self, *args):
        import time
        print(f"Elapsed: {time.time() - self.start:.4f}s")

with Timer():
    sum(range(1_000_000))

import os
for fn in ["data.txt", "in.txt", "out.txt"]:
    if os.path.exists(fn):
        os.remove(fn)