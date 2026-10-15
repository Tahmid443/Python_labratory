# break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# continue - skip iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# pass - placeholder
for i in range(3):
    pass  # TODO: implement

def todo_function():
    pass

class EmptyClass:
    pass

# Search with break
def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None

# Skip invalid data
def process(values):
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            continue
        total += v
    return total

if __name__ == "__main__":
    print(find_first_even([1, 3, 5, 4, 7]))
    print(process([1, "a", 2, None, 3]))