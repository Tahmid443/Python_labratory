# Overview of common stdlib modules

# os - operating system
import os
print(os.getcwd())

# sys - interpreter
import sys
print(sys.version)

# math
import math
print(math.sqrt(16), math.floor(3.7), math.ceil(3.2))

# random
import random
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))
random.seed(42)
print(random.random())

# datetime
from datetime import datetime, date, timedelta
print(datetime.now())
print(date.today())
print(datetime.now() + timedelta(days=7))

# json
import json
print(json.dumps({"a": 1}))
print(json.loads('{"b": 2}'))

# re
import re
print(re.findall(r"\d+", "abc123def456"))

# collections
from collections import Counter, defaultdict, deque
print(Counter("hello"))
d = defaultdict(int); d["x"] += 1
print(d)

# itertools
from itertools import count, cycle, chain, combinations
print(list(chain([1, 2], [3, 4])))
print(list(combinations([1, 2, 3], 2)))

# functools
from functools import reduce, lru_cache
print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))

# pathlib
from pathlib import Path
print(Path.cwd())