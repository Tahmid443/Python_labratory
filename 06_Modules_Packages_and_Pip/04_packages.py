"""
Package structure example:

mypackage/
├── __init__.py
├── math/
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
└── utils/
    ├── __init__.py
    └── helpers.py
"""

# Simulate package
import types, sys

# Create package
pkg = types.ModuleType("mypackage")
pkg.__path__ = []
sys.modules["mypackage"] = pkg

# Submodule
basic = types.ModuleType("mypackage.basic")
exec("def add(a, b): return a + b\ndef sub(a, b): return a - b", basic.__dict__)
sys.modules["mypackage.basic"] = basic

# __init__.py content
pkg.basic = basic

# Usage
from mypackage import basic
print(basic.add(2, 3))
print(basic.sub(5, 2))

# Real usage:
# from mypackage.math.basic import add
# from mypackage.utils.helpers import format_output