class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = 0
        return cls._instance

a = Singleton()
b = Singleton()
a.value = 42
print(b.value)      # 42
print(a is b)       # True

# Thread-safe with lock
import threading

class SafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

# Module-level singleton (Pythonic)
class _Config:
    def __init__(self):
        self.debug = False

config = _Config()   # imported as singleton