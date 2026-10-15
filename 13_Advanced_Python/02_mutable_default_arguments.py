# The classic gotcha
def bad(item, lst=[]):
    lst.append(item)
    return lst

print(bad(1))   # [1]
print(bad(2))   # [1, 2] - NOT [2]!
print(bad(3))   # [1, 2, 3]

# Fix: use None sentinel
def good(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(good(1))
print(good(2))

# Same for dicts/sets
def bad_dict(key, d={}):
    d[key] = True
    return d

print(bad_dict("a"))   # {'a': True}
print(bad_dict("b"))   # {'a': True, 'b': True}

def good_dict(key, d=None):
    if d is None:
        d = {}
    d[key] = True
    return d

print(good_dict("a"))
print(good_dict("b"))

# Why? Default evaluated once at function definition
def show_default():
    print(show_default.__defaults__)

def f(x, lst=[]):
    lst.append(x)
    print(f.__defaults__)
    return lst

f(1)
f(2)

# Mutable default is OK if never mutated
def read_only(items, cache={}):
    """Not modifying default, using as lookup"""
    key = id(items)
    if key not in cache:
        cache[key] = sum(items)
    return cache[key]

print(read_only([1, 2, 3]))
print(read_only([4, 5]))