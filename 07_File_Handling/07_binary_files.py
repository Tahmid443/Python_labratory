import os

FILENAME = "data.bin"

# Write bytes
data = bytes([0, 1, 2, 3, 255])
with open(FILENAME, "wb") as f:
    f.write(data)

# Read bytes
with open(FILENAME, "rb") as f:
    raw = f.read()
print(raw)
print(list(raw))

# Structured binary (struct)
import struct

with open(FILENAME, "wb") as f:
    f.write(struct.pack("iif", 42, -7, 3.14))   # int, int, float

with open(FILENAME, "rb") as f:
    data = f.read()
    a, b, c = struct.unpack("iif", data)
    print(a, b, c)

# Pickle (Python-specific)
import pickle

obj = {"name": "Alice", "scores": [1, 2, 3]}

with open(FILENAME, "wb") as f:
    pickle.dump(obj, f)

with open(FILENAME, "rb") as f:
    loaded = pickle.load(f)
print(loaded)

os.remove(FILENAME)