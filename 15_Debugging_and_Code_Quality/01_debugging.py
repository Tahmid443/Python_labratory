import pdb

def buggy_function(nums):
    total = 0
    for i, n in enumerate(nums):
        total += n / i    # ZeroDivisionError when i=0
    return total

# Method 1: print debugging
def debug_prints(nums):
    print(f"nums={nums}")
    result = []
    for i, n in enumerate(nums):
        print(f"Processing index {i}, value {n}")
        if n > 0:
            result.append(n * 2)
    print(f"result={result}")
    return result

# Method 2: breakpoint() (Python 3.7+)
def breakpoint_demo(x):
    result = x * 2
    breakpoint()   # pauses here in interactive session
    return result

# Method 3: pdb.set_trace
def pdb_demo():
    x = 1
    y = 2
    # pdb.set_trace()
    return x + y

# Method 4: assertion
def assert_demo(nums):
    assert len(nums) > 0, "Empty list"
    return sum(nums) / len(nums)

# Method 5: logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def logging_demo(x):
    logger.debug(f"Input: {x}")
    result = x ** 2
    logger.debug(f"Result: {result}")
    return result

if __name__ == "__main__":
    print(debug_prints([1, -2, 3, -4]))
    print(assert_demo([1, 2, 3]))
    print(logging_demo(5))