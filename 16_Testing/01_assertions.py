# Basic assertions
def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0

# With message
assert add(2, 3) == 5, "add(2, 3) should be 5"

# Using functions
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("test_add passed")

def test_edge_cases():
    assert add(0, 0) == 0
    assert add(10**9, 10**9) == 2 * 10**9
    print("test_edge_cases passed")

# Property-based checks
def test_commutative():
    for a in range(-10, 11):
        for b in range(-10, 11):
            assert add(a, b) == add(b, a)
    print("test_commutative passed")

if __name__ == "__main__":
    test_add()
    test_edge_cases()
    test_commutative()
    print("All assertions passed!")