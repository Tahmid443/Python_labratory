"""
Run with: pytest 04_fixtures.py -v
"""
import pytest

# Basic fixture
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_len(sample_list):
    assert len(sample_list) == 5

# Yield fixture (setup + teardown)
@pytest.fixture
def temp_file(tmp_path):
    path = tmp_path / "data.txt"
    path.write_text("hello")
    yield path
    # cleanup happens automatically with tmp_path

def test_read_file(temp_file):
    assert temp_file.read_text() == "hello"

# Scope
@pytest.fixture(scope="module")
def expensive():
    print("Creating expensive resource")
    return {"data": [1, 2, 3]}

def test_uses_expensive(expensive):
    assert len(expensive["data"]) == 3

def test_uses_expensive_again(expensive):
    assert expensive["data"][0] == 1

# Parametrized fixture
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_number_is_positive(number):
    assert number > 0

# Autouse
@pytest.fixture(autouse=True)
def setup_environment():
    print("\nSetting up...")
    yield
    print("Tearing down...")

def test_something():
    assert True

# Fixture depending on fixture
@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

@pytest.fixture
def greeting(user):
    return f"Hello, {user['name']}"

def test_greeting(greeting):
    assert greeting == "Hello, Alice"