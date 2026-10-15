import os
FILENAME = "modes.txt"

# Modes demonstration
modes = {
    "r":  "read (default, file must exist)",
    "w":  "write (overwrites, creates)",
    "a":  "append (creates if missing)",
    "x":  "exclusive create (error if exists)",
    "b":  "binary mode (add to other)",
    "t":  "text mode (default)",
    "+":  "read and write",
}

for m, desc in modes.items():
    print(f"{m}: {desc}")

# Write
with open(FILENAME, "w") as f:
    f.write("line1\n")

# Read + write
with open(FILENAME, "r+") as f:
    data = f.read()
    f.seek(0)
    f.write("NEW\n")
    f.write(data)

with open(FILENAME) as f:
    print(f.read())

# Exclusive
try:
    with open(FILENAME, "x") as f:
        f.write("fail")
except FileExistsError:
    print("File already exists!")

os.remove(FILENAME)