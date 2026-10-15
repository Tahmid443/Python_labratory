class Counter:
    # Class variable (shared)
    total = 0

    def __init__(self, name):
        # Instance variable (unique)
        self.name = name
        self.count = 0
        Counter.total += 1

    def increment(self):
        self.count += 1

c1 = Counter("a")
c2 = Counter("b")

c1.increment()
c1.increment()
c2.increment()

print(c1.count, c2.count)   # 2, 1
print(Counter.total)         # 2

# Class variable with mutable value (caution!)
class Team:
    members = []   # BAD! shared across all instances

    def add(self, name):
        self.members.append(name)

t1 = Team()
t2 = Team()
t1.add("Alice")
print(t2.members)   # ['Alice'] - unexpected!

# Fix: initialize in __init__
class GoodTeam:
    def __init__(self):
        self.members = []
    def add(self, name):
        self.members.append(name)

g1 = GoodTeam()
g2 = GoodTeam()
g1.add("Alice")
print(g2.members)   # []

# Accessing class vars
print(Team.members)
print(c1.__class__.total)