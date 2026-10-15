# Assert - for debugging, not production validation
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

print(divide(10, 2))
# divide(10, 0)  # AssertionError

# Post-condition check
def average(nums):
    assert len(nums) > 0, "Empty list"
    result = sum(nums) / len(nums)
    assert 0 <= result <= 100 or True, "Range check"
    return result

# Invariant check
def sort_check(arr):
    sorted_arr = sorted(arr)
    assert sorted_arr == sorted(sorted_arr)
    return sorted_arr

# Disabled with -O flag
# python -O script.py disables assertions

# Better: raise for runtime validation
def production_divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

# Assertions for internal state
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
        assert self._items[-1] == x
    def pop(self):
        assert not self.is_empty(), "Pop from empty"
        return self._items.pop()
    def is_empty(self):
        return len(self._items) == 0

s = Stack()
s.push(1)
print(s.pop())