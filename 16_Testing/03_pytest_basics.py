"""
Run with: pytest 03_pytest_basics.py -v
"""
import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Simple test
def test_add():
    assert add(2, 3) == 5

# Parameterized
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected

# Exception test
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_divide_by_zero_match():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(1, 0)

# Approximate
def test_float():
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

# Skip
@pytest.mark.skip(reason="Not implemented")
def test_future():
    pass

# xfail
@pytest.mark.xfail
def test_expected_fail():
    assert 1 == 2

# Class-based
class TestMath:
    def test_add(self):
        assert add(1, 2) == 3
    def test_sub(self):
        assert add(5, -3) == 2

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))