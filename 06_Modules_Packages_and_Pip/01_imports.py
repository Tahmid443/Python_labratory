# Basic imports
import math
print(math.pi)

# Import specific
from math import pi, sqrt
print(pi, sqrt(16))

# Alias
import math as m
print(m.e)

# Import multiple
from math import pi as PI, e as E
print(PI, E)

# Import all (avoid!)
# from math import *
# print(pi)

# Conditional import
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
print(f"NumPy: {HAS_NUMPY}")

# Relative imports (in packages)
# from . import utils
# from .utils import helper

# __name__ check
if __name__ == "__main__":
    print("Running as script")

# Lazy import (inside function - avoids startup cost)
def do_something():
    import json
    return json.dumps({"ok": True})

print(do_something())