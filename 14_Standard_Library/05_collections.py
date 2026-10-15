from collections import Counter, defaultdict, OrderedDict, deque, namedtuple, ChainMap

# Counter
c = Counter("hello")
print(c)
print(c.most_common(2))
c.update("world")
print(c)

# defaultdict
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
print(d)

counts = defaultdict(int)
for ch in "hello":
    counts[ch] += 1
print(dict(counts))

# deque (double-ended queue)
q = deque([1, 2, 3])
q.appendleft(0)
q.append(4)
q.popleft()
q.pop()
print(q)

# Fixed-size deque
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
print(recent)

# OrderedDict (ordered since 3.7)
od = OrderedDict()
od["b"] = 2
od["a"] = 1
print(od)
od.move_to_end("b")
print(od)

# namedtuple
Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p.x, p.y)
print(p._asdict())

# ChainMap
defaults = {"color": "red", "size": "M"}
user = {"color": "blue"}
cm = ChainMap(user, defaults)
print(cm["color"], cm["size"])