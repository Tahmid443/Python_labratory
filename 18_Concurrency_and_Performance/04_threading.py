import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Basic thread
def worker(name, delay):
    print(f"{name} starting")
    time.sleep(delay)
    print(f"{name} done")

t1 = threading.Thread(target=worker, args=("A", 0.5))
t2 = threading.Thread(target=worker, args=("B", 0.3))
t1.start(); t2.start()
t1.join(); t2.join()

# ThreadPoolExecutor
def fetch(url):
    time.sleep(0.1)
    return f"data from {url}"

urls = [f"url{i}" for i in range(5)]

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(fetch, urls))
print(f"Time: {time.perf_counter() - start:.2f}s")
print(results)

# Lock (mutex)
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Counter: {counter}")

# Event
event = threading.Event()

def waiter():
    print("Waiting...")
    event.wait()
    print("Released!")

def setter():
    time.sleep(0.5)
    event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()
time.sleep(1)

# When to use threads
# - I/O bound tasks (network, disk)
# - Not for CPU-bound (GIL blocks)