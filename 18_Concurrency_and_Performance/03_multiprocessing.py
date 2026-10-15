import multiprocessing as mp
import time

def cpu_task(n):
    return sum(i * i for i in range(n))

def worker(x):
    time.sleep(0.1)
    return x * x

if __name__ == "__main__":
    # Get CPU count
    print(f"CPUs: {mp.cpu_count()}")

    # Sequential
    start = time.perf_counter()
    results = [cpu_task(1_000_000) for _ in range(4)]
    print(f"Sequential: {time.perf_counter() - start:.2f}s")

    # Parallel
    start = time.perf_counter()
    with mp.Pool(4) as pool:
        results = pool.map(cpu_task, [1_000_000] * 4)
    print(f"Parallel: {time.perf_counter() - start:.2f}s")

    # Process
    p = mp.Process(target=worker, args=(5,))
    p.start()
    p.join()

    # Queue
    q = mp.Queue()
    def producer(q):
        for i in range(5):
            q.put(i)
    def consumer(q):
        while True:
            item = q.get()
            if item is None:
                break
            print(f"Got: {item}")
    p1 = mp.Process(target=producer, args=(q,))
    p2 = mp.Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); q.put(None); p2.join()

    # Shared value
    shared = mp.Value("i", 0)
    lock = mp.Lock()

    def increment(shared, lock):
        for _ in range(1000):
            with lock:
                shared.value += 1

    procs = [mp.Process(target=increment, args=(shared, lock)) for _ in range(4)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(f"Shared value: {shared.value}")