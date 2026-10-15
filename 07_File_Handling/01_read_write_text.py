import os

FILENAME = "sample.txt"

# Write
with open(FILENAME, "w") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")
    f.writelines(["Third\n", "Fourth\n"])

# Read entire
with open(FILENAME, "r") as f:
    content = f.read()
    print(repr(content))

# Read lines
with open(FILENAME) as f:
    lines = f.readlines()
print(lines)

# Iterate line by line (memory efficient)
with open(FILENAME) as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.rstrip()}")

# Append
with open(FILENAME, "a") as f:
    f.write("Appended.\n")

# Cleanup
os.remove(FILENAME)