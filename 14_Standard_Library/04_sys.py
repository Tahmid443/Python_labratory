import sys

# Version
print(sys.version)
print(sys.version_info)

# Platform
print(sys.platform)
print(sys.maxsize)

# Paths
print(sys.path[:3])

# Arguments
print(sys.argv)

# Standard streams
# sys.stdout.write("msg\n")
# sys.stderr.write("error\n")

# Recursion limit
print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)

# Module search
print(sys.modules.get("math"))

# Exit
# sys.exit(0)

# Reference count
x = []
print(sys.getrefcount(x))

# Size of objects
print(sys.getsizeof([]))
print(sys.getsizeof(1))
print(sys.getsizeof("hello"))

# Streamline
print("hi", file=sys.stderr)