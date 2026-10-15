"""
Run with: pytest 05_mocking.py -v
"""
from unittest.mock import Mock, patch, MagicMock, call
import pytest
import requests

# Simple mock
def test_mock_basic():
    m = Mock()
    m.method.return_value = 42
    assert m.method() == 42
    m.method.assert_called_once()

# Mock with side effect
def test_side_effect():
    m = Mock(side_effect=[1, 2, 3])
    assert m() == 1
    assert m() == 2
    assert m() == 3

# Mock raising
def test_mock_raises():
    m = Mock(side_effect=ValueError("bad"))
    with pytest.raises(ValueError):
        m()

# Patch function
def get_weather(city):
    response = requests.get(f"https://api.example.com/{city}")
    return response.json()

def test_get_weather():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"temp": 20}
        result = get_weather("NYC")
        assert result == {"temp": 20}
        mock_get.assert_called_once_with("https://api.example.com/NYC")

# Patch class attribute
class Config:
    DEBUG = False

def test_config():
    with patch.object(Config, "DEBUG", True):
        assert Config.DEBUG is True
    assert Config.DEBUG is False

# MagicMock (supports magic methods)
def test_magic_mock():
    m = MagicMock()
    m.__len__.return_value = 5
    assert len(m) == 5
    m.__getitem__.return_value = "x"
    assert m[0] == "x"

# Assert calls
def test_assert_calls():
    m = Mock()
    m(1, 2)
    m(3, key="val")
    assert m.call_count == 2
    m.assert_any_call(1, 2)
    m.assert_called_with(3, key="val")

# Dependency injection (cleaner)
class Notifier:
    def send(self, msg):
        raise NotImplementedError

def alert(notifier, msg):
    notifier.send(msg)

def test_alert():
    mock = Mock(spec=Notifier)
    alert(mock, "hello")
    mock.send.assert_called_once_with("hello")