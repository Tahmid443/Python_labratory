# range(stop)
print(list(range(5)))       # [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 7)))    # [2, 3, 4, 5, 6]

# range(start, stop, step)
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1))) # [10, 9, ..., 1]

# range is lazy (memory efficient)
r = range(1_000_000)
print(r[500])       # indexing works
print(len(r))       # length works
print(5 in r)       # membership works

# Convert if needed
print(sum(range(101)))  # sum 0..100

# Common patterns
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Multiple ranges
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
print()