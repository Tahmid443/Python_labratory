# 16. Testing in Python

Testing is the process of checking whether your code behaves as expected. Instead of manually running a program and looking at its output every time, you write tests that verify its correctness automatically.

Testing is useful for finding bugs early, preventing old bugs from returning, and making code easier to maintain.

For competitive programming, testing helps you verify algorithms, catch edge cases, and compare your solution against expected results.

## 📁 Project Structure

```text
16_Testing/
├── 01_assertions.py
├── 02_unittest_basics.py
├── 03_pytest_basics.py
├── 04_fixtures.py
└── 05_mocking.py
```

## 🎯 Learning Objectives

After completing this module, you should be able to:

- Write basic assertions to check program correctness.
- Create automated tests using Python's built-in `unittest`.
- Use `pytest` for concise and flexible testing.
- Test multiple inputs using parameterization.
- Use fixtures for reusable test data and setup.
- Mock external dependencies such as APIs.
- Test exceptions, floating-point results, and edge cases.
- Apply systematic testing to competitive programming problems.

---

## 1. Basic Assertions — `01_assertions.py`

An assertion checks whether a condition is true. If the condition is false, Python raises an `AssertionError`.

### 1.1 Simple assertions

```python
def add(a, b):
    return a + b


assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
```

If every assertion succeeds, execution continues normally.

If an assertion fails, Python stops at that assertion unless the exception is handled.

```python
assert add(2, 3) == 6
```

This raises an `AssertionError` because the expected result is incorrect.

### 1.2 Assertions with messages

You can provide a message to explain why an assertion failed.

```python
assert add(2, 3) == 5, "add(2, 3) should be 5"
```

If the condition is false, the message helps identify the problem.

### 1.3 Organizing checks into functions

```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("test_add passed")


def test_edge_cases():
    assert add(0, 0) == 0
    assert add(10**9, 10**9) == 2 * 10**9
    print("test_edge_cases passed")
```

Run the functions to execute the checks:

```python
test_add()
test_edge_cases()
```

For a small learning exercise, this is enough to test a function manually.

For larger projects, testing frameworks provide better reporting, test discovery, and reusable features.

### 1.4 Property-based checks

Sometimes, instead of testing only specific outputs, you can test a property that should always hold.

Addition is commutative:

\[
a+b=b+a
\]

```python
def test_commutative():
    for a in range(-10, 11):
        for b in range(-10, 11):
            assert add(a, b) == add(b, a)

    print("test_commutative passed")
```

This checks the property for all pairs of integers between `-10` and `10`.

It is not an exhaustive proof for all integers, but it tests many cases.

### When should you use basic assertions?

- While learning an algorithm.
- To verify a mathematical result.
- To check invariants during development.
- To compare an optimized solution against a reference implementation.

**Important:** Python can disable `assert` statements when run with optimization, such as `python -O`. Do not use assertions for essential validation that must always execute.

---

## 2. Unit Testing — `02_unittest_basics.py`

`unittest` is Python's built-in unit testing framework. It lets you organize tests into classes, run them automatically, and receive structured test reports.

A unit test checks a small piece of functionality, usually a single function or method.

### 2.1 Writing a basic test class

```python
import unittest


def add(a, b):
    return a + b


class TestMath(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

Key concepts:

- A test class inherits from `unittest.TestCase`.
- Test methods normally begin with `test_`.
- `self.assertEqual(actual, expected)` checks whether two values are equal.
- `unittest.main()` discovers and runs tests in the current module.

Run the file:

```bash
python 02_unittest_basics.py
```

### 2.2 Common `unittest` assertions

| Assertion | Purpose |
|---|---|
| `assertEqual(a, b)` | Checks equality |
| `assertNotEqual(a, b)` | Checks inequality |
| `assertTrue(x)` | Checks that `x` is true |
| `assertFalse(x)` | Checks that `x` is false |
| `assertIsNone(x)` | Checks that `x` is `None` |
| `assertIsNotNone(x)` | Checks that `x` is not `None` |
| `assertIn(x, container)` | Checks membership |
| `assertNotIn(x, container)` | Checks non-membership |
| `assertIsInstance(x, T)` | Checks the object's type |
| `assertListEqual(a, b)` | Checks list equality |
| `assertDictEqual(a, b)` | Checks dictionary equality |
| `assertAlmostEqual(a, b)` | Checks approximate numerical equality |
| `assertRaises(E)` | Checks whether exception `E` is raised |

Example:

```python
self.assertEqual([1, 2], [1, 2])
self.assertIn(2, [1, 2, 3])
self.assertTrue(5 > 2)
```

### 2.3 Testing exceptions

Suppose division by zero is invalid:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
```

Test that the correct exception is raised:

```python
def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
        divide(1, 0)
```

This test passes only if the code inside the context manager raises the expected exception.

You can also check the error message:

```python
def test_divide_error_message(self):
    with self.assertRaisesRegex(ValueError, "divide by zero"):
        divide(1, 0)
```

### 2.4 Testing floating-point results

Floating-point calculations can produce small precision differences.

```python
self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)
```

Approximate comparisons are often more appropriate than exact equality for calculated floating-point values.

### 2.5 Using `setUp()`

The `setUp()` method runs before each test method in a test case.

```python
class TestString(unittest.TestCase):

    def setUp(self):
        self.text = "hello world"

    def test_upper(self):
        self.assertEqual(self.text.upper(), "HELLO WORLD")

    def test_split(self):
        self.assertEqual(self.text.split(), ["hello", "world"])
```

Both tests receive a fresh test instance with the `text` attribute initialized.

### When should you use `unittest`?

- When you want testing without installing an external framework.
- When you prefer class-based organization.
- When you need standard assertions and exception testing.
- When working on a project that already uses `unittest`.

---

## 3. Pytest Basics — `03_pytest_basics.py`

`pytest` is a popular Python testing framework. It supports ordinary Python assertions, automatic test discovery, fixtures, parameterization, and plugins.

Install it with:

```bash
python -m pip install pytest
```

### 3.1 Writing a simple test

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

Unlike `unittest`, a basic pytest test does not require a test class.

Run the test file:

```bash
pytest 03_pytest_basics.py -v
```

The `-v` option provides more detailed test output.

### 3.2 Parameterized tests

Instead of writing a separate test function for every input, use `pytest.mark.parametrize`.

```python
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert a + b == expected
```

Pytest runs the same test function for each row of test data.

This is useful for testing:

- Positive and negative values.
- Empty collections.
- Boundary values.
- Duplicate elements.
- Different algorithm inputs.

### 3.3 Testing exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
```

You can also match part of the exception message:

```python
def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(1, 0)
```

### 3.4 Approximate comparisons

```python
def test_float():
    assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)
```

`pytest.approx()` checks whether the result is sufficiently close to the expected value. The `rel` argument specifies relative tolerance.

### 3.5 Skipping tests

Use `pytest.mark.skip` when a test should not run.

```python
@pytest.mark.skip(reason="Not implemented")
def test_future():
    pass
```

The test is reported as skipped rather than passed.

### 3.6 Expected failures

Use `pytest.mark.xfail` when a test is expected to fail temporarily.

```python
@pytest.mark.xfail(reason="Known bug")
def test_expected_fail():
    assert 1 == 2
```

Pytest normally reports this as an expected failure.

Use `xfail` carefully. It should document a known issue, not hide a test failure indefinitely.

### 3.7 Running pytest

Run a specific file:

```bash
pytest 03_pytest_basics.py -v
```

Run all discoverable tests in the current directory:

```bash
pytest -v
```

Run a test whose name contains a particular expression:

```bash
pytest -k "divide" -v
```

Stop after the first failure:

```bash
pytest -x
```

Show print output even for passing tests:

```bash
pytest -s
```

**Note:** Pytest's default discovery rules usually recognize files named `test_*.py` or `*_test.py`, and functions beginning with `test_`. Your files are named `03_pytest_basics.py` and similar, so run them explicitly as shown, or rename them to conventional test filenames when organizing a larger project.

### `unittest` vs. `pytest`

| Feature | `unittest` | `pytest` |
|---|---|---|
| Included with Python | Yes | No |
| Basic assertions | Special assertion methods | Ordinary `assert` |
| Test classes | Common | Optional |
| Parameterization | Additional patterns or subtests | Built-in decorator |
| Fixtures | `setUp()` and related methods | Flexible fixture system |
| Plugins | More limited ecosystem | Extensive plugin ecosystem |

Both are useful. Start with `unittest` to understand the standard library, then learn pytest for concise testing and flexible fixtures.

---

## 4. Fixtures — `04_fixtures.py`

A fixture provides reusable data, setup, or resources to tests.

Fixtures reduce duplication and help manage things such as temporary files, database connections, and test objects.

Pytest fixtures are declared with `@pytest.fixture`.

### 4.1 A basic fixture

```python
import pytest


@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]


def test_sum(sample_list):
    assert sum(sample_list) == 15


def test_len(sample_list):
    assert len(sample_list) == 5
```

Pytest sees the `sample_list` argument and supplies the fixture with that name.

Each test requests the fixture independently. With the default function scope, the fixture is executed separately for each test.

### 4.2 Fixtures with setup and teardown

A fixture can use `yield` to provide a resource and run cleanup afterward.

```python
@pytest.fixture
def temp_file(tmp_path):
    path = tmp_path / "data.txt"
    path.write_text("hello")

    yield path

    # Additional cleanup can go here.
```

Test it:

```python
def test_read_file(temp_file):
    assert temp_file.read_text() == "hello"
```

The built-in `tmp_path` fixture provides a unique temporary directory for each test. Pytest manages its lifecycle and cleanup.

Because this example uses `tmp_path`, you generally do not need to manually delete the file.

The code after `yield` is useful when you need explicit teardown, such as closing a connection or releasing a resource.

### 4.3 Fixture scopes

Fixtures can be configured to run at different scopes.

```python
@pytest.fixture(scope="module")
def expensive():
    print("Creating expensive resource")
    return {"data": [1, 2, 3]}
```

Common scopes:

| Scope | Lifetime |
|---|---|
| `function` | Once per test function; default |
| `class` | Once per test class |
| `module` | Once per test module |
| `package` | Once per package |
| `session` | Once per test session |

A wider scope can avoid repeated setup, but mutable data may be shared between tests. One test can accidentally affect another if it modifies a shared object.

Choose the narrowest scope that meets your needs.

### 4.4 Parameterized fixtures

A fixture can provide multiple values using `params`.

```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param


def test_number_is_positive(number):
    assert number > 0
```

Pytest runs the test for each fixture parameter.

This is useful when several tests should use the same collection of test values.

### 4.5 Autouse fixtures

An autouse fixture runs automatically for tests within its applicable scope.

```python
@pytest.fixture(autouse=True)
def setup_environment():
    print("\nSetting up...")
    yield
    print("Tearing down...")
```

This fixture runs for each applicable test even when the test does not explicitly request it.

Use autouse fixtures sparingly. Hidden setup can make tests harder to understand.

### 4.6 Fixtures depending on other fixtures

Fixtures can request other fixtures as function arguments.

```python
@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}


@pytest.fixture
def greeting(user):
    return f"Hello, {user['name']}"


def test_greeting(greeting):
    assert greeting == "Hello, Alice"
```

Pytest resolves the dependency and supplies `user` when creating `greeting`.

### When should you use fixtures?

- When multiple tests need the same sample data.
- When tests require temporary files.
- When setup or cleanup is necessary.
- When preparing database or API test environments.
- When tests need reusable, parameterized objects.

---

## 5. Mocking — `05_mocking.py`

Mocking replaces a real dependency with a controlled test object.

It lets you test your code without relying on a live API, database, external service, or expensive operation.

Your file uses `unittest.mock`, which is included in Python's standard library.

Install the additional dependency used by the example:

```bash
python -m pip install requests pytest
```

### 5.1 A basic mock

```python
from unittest.mock import Mock


def test_mock_basic():
    m = Mock()
    m.method.return_value = 42

    assert m.method() == 42
    m.method.assert_called_once()
```

`Mock()` creates an object whose methods and attributes can be configured.

- `return_value` specifies what a call returns.
- `assert_called_once()` checks that a mock was called exactly once.

Mocks can also track arguments:

```python
m = Mock()
m(10, key="value")

m.assert_called_once_with(10, key="value")
```

### 5.2 Using `side_effect`

`side_effect` can provide a sequence of return values:

```python
m = Mock(side_effect=[1, 2, 3])

assert m() == 1
assert m() == 2
assert m() == 3
```

It can also raise an exception:

```python
m = Mock(side_effect=ValueError("bad"))

with pytest.raises(ValueError):
    m()
```

This makes it possible to test how your code handles failures.

### 5.3 Mocking an external API

Consider this function:

```python
import requests


def get_weather(city):
    response = requests.get(
        f"https://api.example.com/{city}"
    )
    return response.json()
```

Calling this function normally makes a network request.

A unit test should not need a live API to check whether `get_weather()` processes the response correctly.

Mock the request:

```python
from unittest.mock import patch


def test_get_weather():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "temp": 20
        }

        result = get_weather("NYC")

        assert result == {"temp": 20}

        mock_get.assert_called_once_with(
            "https://api.example.com/NYC"
        )
```

Inside the `with` block, `requests.get` is replaced with the mock. After the block exits, the original function is restored.

**Important:** Patch the name where the code under test looks it up. If you import a function directly into another module, the correct patch target may be that module's imported name rather than the original defining module.

This example also assumes the `requests` package is installed.

### 5.4 Patching an attribute

```python
from unittest.mock import patch


class Config:
    DEBUG = False


def test_config():
    with patch.object(Config, "DEBUG", True):
        assert Config.DEBUG is True

    assert Config.DEBUG is False
```

`patch.object()` temporarily changes the specified attribute and restores it when the context exits.

### 5.5 `MagicMock`

`MagicMock` supports Python's special methods, such as `__len__` and `__getitem__`.

```python
from unittest.mock import MagicMock


def test_magic_mock():
    m = MagicMock()

    m.__len__.return_value = 5
    assert len(m) == 5

    m.__getitem__.return_value = "x"
    assert m[0] == "x"
```

This is useful when the object being mocked must behave like a list, dictionary, or another object with special methods.

### 5.6 Checking mock calls

```python
from unittest.mock import Mock


def test_assert_calls():
    m = Mock()

    m(1, 2)
    m(3, key="val")

    assert m.call_count == 2

    m.assert_any_call(1, 2)
    m.assert_called_with(3, key="val")
```

These methods verify how the mock was used.

You can also inspect the full call history:

```python
from unittest.mock import call, Mock

m = Mock()
m(1)
m(2)

assert m.call_args_list == [call(1), call(2)]
```

### 5.7 Dependency injection

Instead of importing a dependency globally and patching it, you can pass the dependency into a function.

```python
class Notifier:
    def send(self, msg):
        raise NotImplementedError


def alert(notifier, msg):
    notifier.send(msg)
```

Test it with a mock:

```python
from unittest.mock import Mock


def test_alert():
    mock = Mock(spec=Notifier)

    alert(mock, "hello")

    mock.send.assert_called_once_with("hello")
```

`spec=Notifier` restricts the mock to attributes available on the specified interface.

Dependency injection makes dependencies explicit and often makes testing simpler.

### When should you use mocking?

- To test API clients without making real network requests.
- To simulate database responses.
- To verify that a function called another component correctly.
- To simulate timeouts and failures.
- To test code that depends on expensive or unpredictable services.

**Testing principle:** Mock external boundaries when appropriate, but test your own business logic with real values whenever possible. Excessive mocking can make tests pass even when the actual integration is broken.

---

## 6. Testing Strategy for Competitive Programming

For competitive programming, you usually do not need a large testing framework during a contest. You need a disciplined way to check whether your algorithm is correct.

### 6.1 Test categories

| Test category | Example |
|---|---|
| Normal case | A typical valid input |
| Minimum input | An array with one element |
| Empty input | An empty list, if allowed |
| Boundary values | Minimum or maximum constraints |
| Negative values | Arrays containing negative numbers |
| Duplicate values | `[2, 2, 2]` |
| Already sorted | `[1, 2, 3, 4]` |
| Reverse sorted | `[4, 3, 2, 1]` |
| Large input | Data near the problem's maximum constraint |
| Special structure | All zeros or repeated patterns |

Not every category applies to every problem. Choose test cases based on the input constraints and algorithm.

### 6.2 Compare an optimized solution with a brute-force solution

For a more complex algorithm, a simple brute-force implementation can serve as a reference for small inputs.

For example, suppose you want to test a function that finds the maximum element:

```python
def optimized_max(nums):
    return max(nums)


def brute_force_max(nums):
    best = nums[0]

    for x in nums:
        if x > best:
            best = x

    return best


def test_max():
    cases = [
        [1],
        [1, 2, 3],
        [5, 5, 5],
        [-10, -3, -7],
        [4, -1, 9, 2],
    ]

    for nums in cases:
        assert optimized_max(nums) == brute_force_max(nums)
```

This example compares two implementations, although both are simple. For harder problems, use a straightforward reference algorithm to check an optimized one on many small inputs.

### 6.3 Use random testing carefully

Randomly generated cases can reveal bugs that hand-written tests miss.

However, randomness alone does not prove correctness. Use a fixed seed when you want reproducible tests, and ensure generated cases respect the problem's constraints.

For a reproducible test, Python's `random` module can generate ordinary test data:

```python
import random


def test_random_cases():
    rng = random.Random(42)

    for _ in range(100):
        nums = [
            rng.randint(-100, 100)
            for _ in range(rng.randint(1, 20))
        ]

        assert max(nums) == sorted(nums)[-1]
```

This checks that `max()` agrees with sorting on many generated lists. For your own algorithm, replace `max(nums)` with the function you want to validate.

---

## 7. Common Mistakes

### Mistake 1: Testing only one input

One passing example does not establish correctness.

**Solution:** Include normal cases, edge cases, and boundary values.

### Mistake 2: Writing tests that repeat the same bug

If the expected result is computed using the same incorrect logic as the function under test, the test may pass incorrectly.

**Solution:** Use independently calculated expected results or a separate reference implementation.

### Mistake 3: Using floating-point equality carelessly

Some decimal values cannot be represented exactly in binary floating-point.

**Solution:** Use `assertAlmostEqual()` in `unittest` or `pytest.approx()` in pytest when approximate equality is appropriate.

### Mistake 4: Forgetting fixture scope

A module-scoped fixture may share a mutable object between tests.

**Solution:** Avoid unexpected shared state or use a narrower fixture scope.

### Mistake 5: Mocking the wrong name

Patching a function in the wrong module may leave the real dependency untouched.

**Solution:** Patch the name used by the code under test.

### Mistake 6: Depending on a real API in unit tests

A network outage or API change can make a test fail for reasons unrelated to your code.

**Solution:** Mock the external dependency in unit tests and add separate integration tests when real connectivity needs to be verified.

### Mistake 7: Ignoring skipped or expected-failure tests

A skipped test does not verify correctness, and an expected-failure test may conceal a bug if never revisited.

**Solution:** Review skipped and `xfail` tests regularly.

---

## 8. Practice Checklist

### Assertions

- [ ] Write assertions for a simple mathematical function.
- [ ] Test positive, negative, and boundary values.
- [ ] Verify a property across many input pairs.
- [ ] Understand when assertions can be disabled.

### `unittest`

- [ ] Create a class inheriting from `unittest.TestCase`.
- [ ] Use `assertEqual()` and `assertIn()`.
- [ ] Test that an exception is raised.
- [ ] Use `setUp()` to initialize shared test state.

### `pytest`

- [ ] Run a test file with `pytest -v`.
- [ ] Use `pytest.mark.parametrize`.
- [ ] Test an exception with `pytest.raises()`.
- [ ] Compare floating-point values with `pytest.approx()`.
- [ ] Understand `skip` and `xfail`.

### Fixtures

- [ ] Create a basic fixture.
- [ ] Use `tmp_path` for temporary files.
- [ ] Write a fixture with setup and teardown.
- [ ] Understand fixture scopes.
- [ ] Create a fixture that depends on another fixture.

### Mocking

- [ ] Set a mock's `return_value`.
- [ ] Use `side_effect` to simulate a failure.
- [ ] Patch an external API call.
- [ ] Check how many times a mock was called.
- [ ] Test a function using dependency injection.

### Competitive programming

- [ ] Test the smallest valid input.
- [ ] Test duplicate and negative values when permitted.
- [ ] Compare an optimized algorithm with a brute-force reference.
- [ ] Use reproducible random tests for small inputs.
- [ ] Confirm the final output format matches the problem statement.

---

## 9. Mini Project — Test a Binary Search Implementation

Write a binary search function and test its correctness using `pytest`.

Create a file named `binary_search.py`:

```python
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Binary search requires the input list to be sorted in ascending order.

Create a test file named `test_binary_search.py`:

```python
import pytest
from binary_search import binary_search


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 4, -1),
        ([10], 10, 0),
        ([10], 5, -1),
        ([], 10, -1),
    ],
)
def test_binary_search(nums, target, expected):
    assert binary_search(nums, target) == expected
```

Run the tests:

```bash
pytest test_binary_search.py -v
```

### Mini project challenges

1. Test a target smaller than every element.
2. Test a target larger than every element.
3. Test a list containing duplicate values. The current implementation may return any matching index.
4. Add a separate function that returns the first occurrence of a target.
5. Deliberately introduce an off-by-one error and verify that your tests catch it.

---

## 10. Suggested Learning Order

1. **Assertions:** Learn to express expected behavior.
2. **`unittest`:** Understand test cases, assertion methods, and exception testing.
3. **`pytest`:** Learn concise test functions and parameterization.
4. **Fixtures:** Organize reusable test data and resource setup.
5. **Mocking:** Isolate external dependencies and test failure handling.
6. **Algorithm testing:** Use boundary cases, brute-force comparisons, and random test generation.

## Final Takeaway

Testing and debugging work together:

- **Debugging** helps you discover why a program is wrong.
- **Testing** helps you detect incorrect behavior and prevent regressions.
- **Fixtures** make test setup reusable.
- **Mocking** isolates dependencies that are difficult or expensive to run.
- **Property checks and randomized testing** help you explore a wider range of inputs.

For competitive programming, make testing part of your problem-solving process: write the algorithm, verify it with small examples, test edge cases, and compare it with a simple reference solution whenever possible.