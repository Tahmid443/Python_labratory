from contextlib import contextmanager

# Class-based
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False

with FileManager("test.txt", "w") as f:
    f.write("hello")

# Generator-based (simpler)
@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_manager("test.txt", "r") as f:
    print(f.read())

# Database transaction example
@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

# Suppressing errors
@contextmanager
def suppress(*exceptions):
    try:
        yield
    except exceptions:
        pass

with suppress(ValueError):
    int("abc")
print("Continued")

# Timing
import time
@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")

with timer("Work"):
    sum(range(1000000))

# Temporary directory
import tempfile, os
@contextmanager
def temp_dir():
    import tempfile, shutil
    d = tempfile.mkdtemp()
    try:
        yield d
    finally:
        shutil.rmtree(d)

with temp_dir() as d:
    print(f"Temp dir: {d}")

os.remove("test.txt")