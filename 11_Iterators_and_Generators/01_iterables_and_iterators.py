# Iterable: object with __iter__
# Iterator: object with __iter__ and __next__

# Iterables
for x in [1, 2, 3]:
    pass

# Get iterator
lst = [1, 2, 3]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
# next(it)  # StopIteration

# Custom iterator
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(5):
    print(n, end=" ")
print()

# Custom iterable (separate iterator)
class MyRange:
    def __init__(self, start, end):
        self.start, self.end = start, end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

for n in MyRange(1, 5):
    print(n, end=" ")
print()

# Check protocol
print(hasattr([1, 2], "__iter__"))       # True
print(hasattr(iter([1, 2]), "__next__")) # True