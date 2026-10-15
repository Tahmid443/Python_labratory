import cProfile
import pstats
import io

def slow_function():
    total = 0
    for i in range(100000):
        total += i ** 2
    return total

def medium_function():
    return sum(range(50000))

def main():
    for _ in range(10):
        slow_function()
    for _ in range(50):
        medium_function()

# Profile
profiler = cProfile.Profile()
profiler.enable()
main()
profiler.disable()

# Print stats
s = io.StringIO()
ps = pstats.Stats(profiler, stream=s).sort_stats("cumulative")
ps.print_stats(10)
print(s.getvalue())

# Save for later analysis
profiler.dump_stats("profile.prof")
# Analyze: python -m pstats profile.prof

# Line-by-line (line_profiler)
# pip install line_profiler
# @profile decorator then: kernprof -l -v script.py

# Memory profiler
# pip install memory_profiler
# @profile decorator then: python -m memory_profiler script.py

import os
if os.path.exists("profile.prof"):
    os.remove("profile.prof")