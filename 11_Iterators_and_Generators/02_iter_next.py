# next with default
it = iter([1, 2, 3])
print(next(it))
print(next(it))
print(next(it, "default"))
print(next(it, "default"))   # StopIteration avoided

# Infinite iterator
def infinite():
    n = 0
    while True:
        yield n
        n += 1

it = infinite()
print(next(it), next(it), next(it))

# Break out manually
it = iter("hello")
while True:
    try:
        ch = next(it)
        print(ch, end=" ")
    except StopIteration:
        break
print()

# Enumerate implementation
def my_enumerate(iterable, start=0):
    i = start
    for x in iterable:
        yield i, x
        i += 1

print(list(my_enumerate("abc")))

# Zip implementation
def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        values = []
        for it in iterators:
            try:
                values.append(next(it))
            except StopIteration:
                return
        yield tuple(values)

print(list(my_zip([1, 2], "ab", (True, False))))