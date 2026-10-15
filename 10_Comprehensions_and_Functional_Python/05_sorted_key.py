# Basic sorting
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(nums))
print(sorted(nums, reverse=True))

# Key functions
words = ["banana", "apple", "cherry"]
print(sorted(words, key=len))
print(sorted(words, key=str.lower))
print(sorted(words, key=lambda w: w[-1]))    # last char

# Multiple criteria
data = [("Alice", 30), ("Bob", 25), ("Charlie", 30)]
print(sorted(data, key=lambda p: (p[1], p[0])))

# Stable sort
print(sorted(data, key=lambda p: p[1]))

# Sorting dictionaries
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
print(sorted(people, key=lambda p: p["age"]))

# from operator import itemgetter, attrgetter
from operator import itemgetter, attrgetter

print(sorted(data, key=itemgetter(1)))
print(sorted(people, key=itemgetter("age")))

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

points = [Point(1, 2), Point(3, 1), Point(2, 3)]
print(sorted(points, key=attrgetter("y")))

# sorted vs list.sort
original = [3, 1, 2]
new = sorted(original)   # returns new list
original.sort()          # in-place

# Complex key
def score(item):
    return (-item["age"], item["name"])

print(sorted(people, key=score))