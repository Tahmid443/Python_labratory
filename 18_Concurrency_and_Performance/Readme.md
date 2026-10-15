# 18. Concurrency and Performance in Python

This module covers how to measure program execution time, profile performance bottlenecks, and execute tasks using multiprocessing, multithreading, and asynchronous programming.

These concepts help you write efficient Python programs, understand how tasks execute, and choose the right approach for different workloads.

## 📁 Project Structure

```text
18_Concurrency_and_Performance/
├── 01_timeit_profiling.py
├── 02_cprofile.py
├── 03_multiprocessing.py
├── 04_threading.py
├── 05_asyncio_basics.py
├── 06_async_await.py
└── 07_async_tasks.py
```

## 🎯 Learning Objectives

After completing this module, you should be able to:

- Measure execution time using `timeit` and `time.perf_counter()`.
- Profile a program using `cProfile` and `pstats`.
- Understand the difference between concurrency and parallelism.
- Execute CPU-intensive tasks using multiple processes.
- Execute I/O-intensive tasks using multiple threads.
- Understand Python's Global Interpreter Lock (GIL).
- Write asynchronous functions using `async` and `await`.
- Run multiple coroutines concurrently using `asyncio`.
- Create, cancel, and manage asynchronous tasks.
- Use queues, locks, events, and semaphores.
- Select an appropriate execution model for a problem.

---

## 1. Measuring Execution Time with `timeit`

**File:** `01_timeit_profiling.py`

The `timeit` module measures how long a small piece of Python code takes to execute.

It is particularly useful when comparing alternative implementations of the same operation.

### Basic Usage

```python
import timeit

execution_time = timeit.timeit(
    "sum(range(100))",
    number=10000
)

print(f"Execution time: {execution_time:.4f} seconds")
```

- `stmt`: The statement to execute.
- `number`: The number of executions.
- The returned value is the total time in seconds.

### Comparing Implementations

```python
import timeit

def list_comp():
    return [x ** 2 for x in range(100)]

def map_lambda():
    return list(map(lambda x: x ** 2, range(100)))

t1 = timeit.timeit(list_comp, number=10000)
t2 = timeit.timeit(map_lambda, number=10000)

print("List comprehension:", t1)
print("Map and lambda:", t2)
```

Pass a callable directly to `timeit.timeit()` when benchmarking a function.

### Repeating Measurements

```python
import timeit

times = timeit.repeat(
    "sum(range(100))",
    number=1000,
    repeat=5
)

print("Minimum:", min(times))
print("Average:", sum(times) / len(times))
```

Repeated measurements help reduce the influence of temporary system activity. The minimum can be useful for estimating performance under relatively favorable conditions, while the average shows the mean across the measured runs.

### `timeit` vs. `time.perf_counter()`

| Feature | `timeit` | `time.perf_counter()` |
|---|---|---|
| Main purpose | Benchmarking code | Measuring elapsed time |
| Repeated execution | Built-in support | Manual loop required |
| Setup support | Yes | Manual |
| Best use | Small performance comparisons | Timing larger operations |

Example using `time.perf_counter()`:

```python
import time

start = time.perf_counter()

total = sum(range(1_000_000))

elapsed = time.perf_counter() - start

print("Total:", total)
print(f"Elapsed: {elapsed:.4f} seconds")
```

**Important:** Use `timeit` for small benchmarks rather than relying on a single execution measured with `time.time()`.

---

## 2. Profiling with `cProfile`

**File:** `02_cprofile.py`

Benchmarking tells you how long code takes. Profiling helps identify which functions consume the most execution time.

Python provides the built-in `cProfile` module for deterministic profiling.

### Basic Profiling

```python
import cProfile

def calculate():
    total = 0

    for i in range(100_000):
        total += i * i

    return total

cProfile.run("calculate()")
```

The output includes information such as:

- `ncalls`: Number of function calls.
- `tottime`: Time spent inside a function, excluding subcalls.
- `cumtime`: Cumulative time spent in a function, including subcalls.
- `percall`: Average time per call, depending on the displayed column.

### Profiling a Program

```python
import cProfile
import pstats

def main():
    for _ in range(10):
        sum(i * i for i in range(100_000))

profiler = cProfile.Profile()

profiler.enable()
main()
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(10)
```

`sort_stats("cumulative")` places functions with high cumulative time near the top.

You can also sort by internal execution time:

```python
stats.sort_stats("tottime")
stats.print_stats(10)
```

### Saving Profiling Results

```python
import cProfile

cProfile.run("main()", "profile.prof")
```

Analyze the saved profile later:

```bash
python -m pstats profile.prof
```

### Additional Profiling Tools

- `cProfile`: Function-level profiling included with Python.
- `line_profiler`: Measures execution time line by line; requires installation.
- `memory_profiler`: An optional tool for examining memory usage.

### Performance Optimization Workflow

1. Write a correct implementation.
2. Measure its execution time.
3. Profile the program.
4. Identify the actual bottleneck.
5. Optimize the bottleneck.
6. Measure again to verify the improvement.

**Rule:** Do not optimize code solely because it looks slow or complicated. Measure first.

---

## 3. Multiprocessing

**File:** `03_multiprocessing.py`

Multiprocessing uses separate operating-system processes to execute work. Processes have separate memory spaces and can execute Python code on multiple CPU cores.

It is especially useful for **CPU-bound tasks**.

Examples include:

- Large numerical computations.
- Independent simulations.
- Processing many separate files.
- CPU-heavy data transformations.

### Creating a Process

```python
import multiprocessing as mp

def worker(number):
    result = number * number
    print(result)

if __name__ == "__main__":
    process = mp.Process(
        target=worker,
        args=(5,)
    )

    process.start()
    process.join()
```

Important methods:

- `start()`: Starts the process.
- `join()`: Waits for the process to finish.
- `is_alive()`: Checks whether the process is running.
- `terminate()`: Requests termination of the process.

Always use the `if __name__ == "__main__":` guard for multiprocessing program entry points. It is particularly important on platforms that start workers using the `spawn` method.

Worker functions should generally be defined at module scope so they can be imported by worker processes.

### Using a Process Pool

A process pool manages a group of worker processes.

```python
import multiprocessing as mp

def square(number):
    return number * number

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with mp.Pool(processes=4) as pool:
        results = pool.map(square, numbers)

    print(results)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Useful pool methods:

| Method | Purpose |
|---|---|
| `map()` | Applies a function to every input and returns results in input order |
| `starmap()` | Calls a function using multiple arguments from each input |
| `apply()` | Executes a function for one set of arguments |
| `imap()` | Lazily iterates over results in input order |
| `imap_unordered()` | Iterates over results as they become available, without preserving input order |

### Process Communication with Queues

Separate processes cannot ordinarily share normal Python variables directly. A queue allows them to exchange objects.

```python
import multiprocessing as mp

def producer(queue):
    for number in range(5):
        queue.put(number)

    queue.put(None)

def consumer(queue):
    while True:
        item = queue.get()

        if item is None:
            break

        print("Received:", item)

if __name__ == "__main__":
    queue = mp.Queue()

    p1 = mp.Process(target=producer, args=(queue,))
    p2 = mp.Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

The `None` value acts as a sentinel indicating that the producer has finished.

### Shared Memory and Locks

Multiprocessing also provides shared values and arrays. Locks can protect updates that must happen together.

```python
import multiprocessing as mp

def increment(shared_value, lock):
    for _ in range(1000):
        with lock:
            shared_value.value += 1

if __name__ == "__main__":
    shared_value = mp.Value("i", 0)
    lock = mp.Lock()

    processes = [
        mp.Process(
            target=increment,
            args=(shared_value, lock)
        )
        for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(shared_value.value)  # 4000
```

The lock prevents simultaneous read-modify-write operations from losing updates.

### Multiprocessing: Advantages and Disadvantages

**Advantages**
- Can run CPU-bound Python code on multiple cores.
- Processes have separate memory spaces.
- A failure in one worker is less likely to corrupt another process's private memory.

**Disadvantages**
- Creating processes has overhead.
- Data must often be serialized and transferred between processes.
- Shared state and synchronization require additional care.
- Small tasks may run slower in parallel because of overhead.

---

## 4. Multithreading

**File:** `04_threading.py`

Multithreading allows multiple threads to exist inside one process.

Threads share the process's memory, making communication convenient, but shared mutable state must be handled carefully.

Threads are useful for **I/O-bound tasks**, such as:

- Network requests.
- File operations.
- Waiting for database responses.
- Multiple independent I/O operations.

### Creating Threads

```python
import threading
import time

def worker(name):
    print(name, "started")
    time.sleep(1)
    print(name, "finished")

if __name__ == "__main__":
    t1 = threading.Thread(target=worker, args=("A",))
    t2 = threading.Thread(target=worker, args=("B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All threads finished")
```

The threads can overlap while waiting for their respective delays.

### Using `ThreadPoolExecutor`

For many similar tasks, a thread pool is usually more convenient than manually creating each thread.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def fetch_data(item):
    time.sleep(0.5)
    return f"Data for {item}"

items = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_data, items))

print(results)
```

`executor.map()` returns results in input order, even if tasks complete in a different order.

### Race Conditions and Locks

A race condition occurs when the result depends on the timing of concurrent operations.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter

    for _ in range(10_000):
        with lock:
            counter += 1

threads = [
    threading.Thread(target=increment)
    for _ in range(5)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)  # 50000
```

The `with lock:` statement acquires the lock and releases it when the block exits, including when an exception occurs.

Keep locked sections as short as practical.

### Thread Synchronization Tools

| Tool | Purpose |
|---|---|
| `Lock` | Allows one thread at a time into a protected section |
| `RLock` | Reentrant lock that can be acquired multiple times by its owning thread |
| `Event` | Lets threads wait for a shared signal |
| `Semaphore` | Limits the number of threads accessing a resource |
| `Condition` | Coordinates threads based on a condition |
| `Queue` | Safely exchanges work between threads |

Example using an event:

```python
import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for signal...")
    event.wait()
    print("Signal received!")

thread = threading.Thread(target=waiter)
thread.start()

time.sleep(1)
event.set()

thread.join()
```

### The Global Interpreter Lock (GIL)

In conventional CPython builds with the GIL enabled, the Global Interpreter Lock restricts how many threads can execute Python bytecode simultaneously within one interpreter.

Consequently:

- Threads are often effective for I/O-bound work.
- Multiprocessing is often preferable for CPU-bound Python work.
- Threads can still improve throughput when tasks spend time waiting for I/O.
- Some native extensions release the GIL during computation.
- Python also supports optional free-threaded builds, so GIL behavior is not identical in every configuration.

Do not assume that adding more threads will automatically make a CPU-heavy algorithm faster.

---

## 5. Asynchronous Programming with `asyncio`

**File:** `05_asyncio_basics.py`

Asynchronous programming lets a single thread manage multiple operations that spend time waiting, without blocking the entire event loop during each wait.

Python's `asyncio` is particularly useful for large numbers of concurrent I/O operations.

Examples include:

- Network clients and servers.
- Asynchronous HTTP requests.
- WebSocket applications.
- Concurrent database operations with an async driver.

### Defining a Coroutine

```python
import asyncio

async def greet(name):
    print(f"Hello, {name}")

    await asyncio.sleep(1)

    print(f"Goodbye, {name}")

asyncio.run(greet("Alice"))
```

Key concepts:

- `async def`: Defines a coroutine function.
- Calling the function creates a coroutine object.
- `await`: Suspends the current coroutine until the awaited operation completes.
- `asyncio.run()`: Runs a coroutine using an event loop.

`asyncio.sleep()` is an asynchronous sleep. It allows other scheduled coroutines to run while the current coroutine waits.

### Sequential Execution

```python
import asyncio

async def task(name, delay):
    print(name, "started")
    await asyncio.sleep(delay)
    print(name, "finished")

async def main():
    await task("A", 1)
    await task("B", 1)
    await task("C", 1)

asyncio.run(main())
```

Each task is awaited before the next begins, so their delays occur sequentially.

### Concurrent Execution with `asyncio.gather()`

```python
import asyncio

async def task(name, delay):
    print(name, "started")
    await asyncio.sleep(delay)
    print(name, "finished")

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 1),
        task("C", 1)
    )

asyncio.run(main())
```

The three coroutines can overlap their waiting periods. Their combined elapsed time can be close to the longest individual delay, rather than the sum of all delays.

Actual elapsed time depends on the workload and system conditions.

### Important Limitation

`asyncio` does not automatically make CPU-intensive code run in parallel.

Consider:

```python
async def slow_cpu_task():
    total = 0

    for i in range(10_000_000):
        total += i * i

    return total
```

This function performs its calculation without reaching an `await`. While it runs, it blocks the event loop.

For CPU-heavy operations, consider multiprocessing or an appropriate executor.

---

## 6. `async` and `await` in Detail

**File:** `06_async_await.py`

### Returning Data from a Coroutine

```python
import asyncio

async def fetch_data(item_id, delay):
    await asyncio.sleep(delay)

    return {
        "id": item_id,
        "data": f"result-{item_id}"
    }

async def main():
    result = await fetch_data(1, 0.5)
    print(result)

asyncio.run(main())
```

Awaiting the coroutine gives you its return value.

### Running Multiple Operations with `gather()`

```python
import asyncio

async def fetch_data(item_id, delay):
    await asyncio.sleep(delay)
    return f"result-{item_id}"

async def main():
    results = await asyncio.gather(
        fetch_data(1, 0.5),
        fetch_data(2, 0.3),
        fetch_data(3, 0.4)
    )

    print(results)

asyncio.run(main())
```

The returned list preserves the order of the awaitables supplied to `gather()`, not their completion order.

### Timeouts

Use a timeout when an operation must not wait indefinitely.

```python
import asyncio

async def slow_operation():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(
            slow_operation(),
            timeout=1
        )
    except TimeoutError:
        print("Operation timed out")

asyncio.run(main())
```

In modern Python, `asyncio.TimeoutError` is an alias of the built-in `TimeoutError`.

When `wait_for()` times out, it normally cancels the awaited operation and waits for cancellation to finish. A coroutine that handles cancellation unusually may affect the exact elapsed time.

### Cancelling a Task

```python
import asyncio

async def worker():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Worker cancelled")
        raise

async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(0.1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Cancellation handled")

asyncio.run(main())
```

Cancellation is cooperative. Coroutines should clean up resources when necessary and generally re-raise `CancelledError` after performing cleanup.

### Handling Exceptions with `gather()`

```python
import asyncio

async def may_fail(number):
    if number == 2:
        raise ValueError("Something went wrong")

    return number

async def main():
    results = await asyncio.gather(
        may_fail(1),
        may_fail(2),
        may_fail(3),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, BaseException):
            print("Error:", result)
        else:
            print("Result:", result)

asyncio.run(main())
```

When `return_exceptions=True`, exceptions are returned as list entries instead of being propagated immediately by `gather()`.

Handle those entries deliberately rather than treating every result as successful data.

---

## 7. Managing Asynchronous Tasks

**File:** `07_async_tasks.py`

A coroutine describes asynchronous work. A task schedules a coroutine to run on the event loop.

### Creating Tasks

```python
import asyncio

async def worker(name, delay):
    print(name, "started")

    await asyncio.sleep(delay)

    print(name, "finished")
    return f"{name}-result"

async def main():
    task1 = asyncio.create_task(worker("A", 1))
    task2 = asyncio.create_task(worker("B", 0.5))

    print("Other work can happen here")

    result1 = await task1
    result2 = await task2

    print(result1, result2)

asyncio.run(main())
```

`asyncio.create_task()` schedules a coroutine to run concurrently with other work on the same event loop.

Retain references to important tasks and await them or otherwise handle their completion and exceptions.

### Using `asyncio.TaskGroup()` — Python 3.11+

A task group provides structured concurrency: child tasks belong to a scope, and leaving the scope waits for them to finish.

```python
import asyncio

async def worker(name, delay):
    await asyncio.sleep(delay)
    print(name, "finished")
    return f"{name}-result"

async def main():
    async with asyncio.TaskGroup() as group:
        task1 = group.create_task(worker("A", 1))
        task2 = group.create_task(worker("B", 0.5))

    print(task1.result())
    print(task2.result())

asyncio.run(main())
```

Important behavior:

- The task group waits for its child tasks when the context exits.
- If a child task raises an ordinary exception, the group normally cancels its remaining unfinished tasks.
- Exceptions are reported as an exception group.
- Catch grouped exceptions with `except*` when appropriate.

### Asynchronous Queues

`asyncio.Queue` allows asynchronous producers and consumers to exchange work without blocking the event loop while waiting for an item.

```python
import asyncio

async def producer(queue):
    for number in range(5):
        await queue.put(number)

    await queue.put(None)

async def consumer(queue):
    while True:
        item = await queue.get()

        try:
            if item is None:
                return

            print("Consumed:", item)
        finally:
            queue.task_done()

async def main():
    queue = asyncio.Queue()

    async with asyncio.TaskGroup() as group:
        group.create_task(producer(queue))
        group.create_task(consumer(queue))

    await queue.join()

asyncio.run(main())
```

The sentinel `None` tells the consumer that production has ended. Calling `task_done()` for each retrieved item allows `queue.join()` to track completed work.

For production code, consider how to stop multiple consumers and handle exceptions or cancelled tasks safely.

### Limiting Concurrency with a Semaphore

```python
import asyncio

async def limited_work(semaphore, number):
    async with semaphore:
        print("Started:", number)
        await asyncio.sleep(1)
        print("Finished:", number)

async def main():
    semaphore = asyncio.Semaphore(2)

    await asyncio.gather(
        *[
            limited_work(semaphore, number)
            for number in range(5)
        ]
    )

asyncio.run(main())
```

At most two coroutines can hold the semaphore at the same time.

This is useful for limiting concurrent network requests, API calls, or access to a constrained resource.

---

## 8. Concurrency vs. Parallelism

These terms describe different concepts.

**Concurrency:** Multiple tasks make progress during overlapping periods. Their execution can be interleaved.

**Parallelism:** Multiple tasks execute at the same time, such as on separate CPU cores.

| Approach | Execution model | Typical use |
|---|---|---|
| Sequential code | One operation after another | Simple workflows |
| Threading | Multiple threads in one process | I/O-bound work |
| Multiprocessing | Multiple processes | CPU-bound work |
| `asyncio` | Cooperative tasks on an event loop | Many asynchronous I/O operations |

These are general guidelines rather than absolute rules. The best choice depends on the task, the libraries involved, the amount of work, and the overhead of scheduling or communication.

### Choosing the Right Approach

- **Small competitive programming problem:** Usually use ordinary sequential Python.
- **CPU-heavy computation:** Consider algorithmic optimization first, then multiprocessing if tasks can be divided efficiently.
- **Many blocking I/O operations:** Consider threads or a thread pool.
- **Many asynchronous network operations:** Consider `asyncio` and async-compatible libraries.
- **Waiting for one operation:** Concurrency may provide no benefit.
- **Tiny tasks:** Scheduling and communication overhead may exceed the savings.

---

## 9. Common Mistakes

### Mistake 1: Assuming Concurrency Always Improves Speed

Adding threads, processes, or coroutines creates overhead.

**Better approach:** Benchmark the sequential version first, then compare.

### Mistake 2: Forgetting the Multiprocessing Main Guard

Problematic pattern:

```python
# Avoid creating processes at module import time.
process = mp.Process(target=worker)
process.start()
```

Use:

```python
if __name__ == "__main__":
    process = mp.Process(target=worker)
    process.start()
    process.join()
```

Also keep worker functions importable at module scope.

### Mistake 3: Sharing Mutable State Without Synchronization

Two threads or processes may update shared state at the same time.

**Better approach:** Use locks, queues, or a design that avoids shared mutable state.

### Mistake 4: Calling a Coroutine Without Awaiting or Scheduling It

```python
async def greet():
    print("Hello")

greet()  # Creates a coroutine object but does not run it to completion.
```

Correct:

```python
import asyncio

async def greet():
    print("Hello")

asyncio.run(greet())
```

Inside an existing coroutine, use `await greet()` or schedule it as a task when concurrency is needed.

### Mistake 5: Using Blocking Calls Inside Async Code

A blocking `time.sleep()` pauses the event-loop thread.

Use:

```python
await asyncio.sleep(1)
```

Likewise, use asynchronous libraries for I/O where possible. Blocking calls may sometimes be delegated to an executor.

### Mistake 6: Forgetting to Await Tasks

Creating a task does not mean the work has successfully completed.

**Better approach:** Await the task, use a task group, or deliberately manage its lifecycle and exceptions.

### Mistake 7: Ignoring Exceptions in Background Work

Failures in threads, processes, and asynchronous tasks must be collected or reported appropriately.

**Better approach:** Retrieve results from futures, await tasks, and use suitable exception-handling strategies.

### Mistake 8: Optimizing Without Measuring

An implementation that looks more sophisticated may be slower.

**Better approach:** Measure, profile, change one thing, and measure again.

---

## 10. Performance and Complexity

Concurrency does not automatically change the algorithmic time complexity of a task.

For example, summing a list of \(n\) elements still requires \(O(n)\) total element-processing work, even if the work is divided among several processes.

Parallel execution may reduce elapsed time for suitable workloads, but the improvement depends on factors such as:

- Number of CPU cores.
- Task size.
- Scheduling overhead.
- Data transfer and serialization.
- Synchronization.
- Memory bandwidth.
- I/O latency.

For competitive programming, algorithmic complexity is usually more important than concurrency. An \(O(n \log n)\) solution will generally be preferable to an \(O(n^2)\) solution that merely uses more workers, particularly under strict execution limits.

---

## 11. Competitive Programming Notes

Most Codeforces and similar programming contest problems expect a single process executing a normal algorithm. You generally do not need `threading`, `multiprocessing`, or `asyncio`.

Prioritize these skills:

1. Choose an efficient algorithm.
2. Analyze time and space complexity.
3. Use appropriate data structures.
4. Avoid unnecessary loops, copies, and allocations.
5. Use fast input methods when input is large.
6. Benchmark local alternatives when performance is uncertain.
7. Read the problem's execution limits and language requirements.

For ordinary Python contest solutions, efficient algorithms, `sys.stdin.buffer.readline`, and suitable data structures are usually much more valuable than concurrency.

Example:

```python
import sys

def solve():
    input = sys.stdin.buffer.readline

    n = int(input())
    numbers = list(map(int, input().split()))

    print(sum(numbers))

if __name__ == "__main__":
    solve()
```

Use concurrency when a problem or application actually benefits from it—not as a default optimization technique.

---

## 12. Practice Checklist

### Timing and Profiling

- [ ] Measure a function with `timeit.timeit()`.
- [ ] Compare two implementations of the same operation.
- [ ] Repeat a benchmark and compare minimum and average times.
- [ ] Measure elapsed time using `time.perf_counter()`.
- [ ] Profile a program with `cProfile`.
- [ ] Sort profiling statistics by cumulative time and internal time.

### Multiprocessing

- [ ] Create a process with `multiprocessing.Process`.
- [ ] Explain why `start()` and `join()` are different.
- [ ] Use `Pool.map()` to distribute independent work.
- [ ] Pass data through a multiprocessing queue.
- [ ] Protect shared-value updates with a lock.
- [ ] Explain process startup and serialization overhead.

### Threading

- [ ] Create and join multiple threads.
- [ ] Use `ThreadPoolExecutor`.
- [ ] Demonstrate a race condition conceptually.
- [ ] Protect shared state with a lock.
- [ ] Coordinate threads using an event.
- [ ] Explain why threads are often useful for I/O-bound tasks.

### Asynchronous Programming

- [ ] Write an `async def` coroutine.
- [ ] Run a coroutine with `asyncio.run()`.
- [ ] Explain what `await` does.
- [ ] Compare sequential awaits with `asyncio.gather()`.
- [ ] Create tasks using `asyncio.create_task()`.
- [ ] Apply a timeout using `asyncio.wait_for()`.
- [ ] Cancel a task and handle cancellation correctly.
- [ ] Use `asyncio.TaskGroup()` on Python 3.11 or later.
- [ ] Coordinate producers and consumers with `asyncio.Queue`.
- [ ] Limit concurrent work with `asyncio.Semaphore`.

---

## 13. Mini Projects

Try completing these projects without copying the existing examples.

### Project 1: Benchmark Comparison

Write three functions that compute the squares of numbers using:

- A regular `for` loop.
- A list comprehension.
- `map()` with a function.

Use `timeit` to compare their execution times for several input sizes.

**Goal:** Learn to measure performance instead of guessing.

### Project 2: Parallel CPU Work

Divide a CPU-intensive calculation into independent chunks. Compare a sequential implementation against a multiprocessing implementation.

Measure both versions and explain any overhead or speed difference you observe.

**Goal:** Understand when parallel processing is useful.

### Project 3: Concurrent I/O Simulator

Create multiple simulated I/O tasks using `asyncio.sleep()`. Compare sequential execution against concurrent execution with `asyncio.gather()`.

Then limit the number of simultaneous tasks using a semaphore.

**Goal:** Understand asynchronous concurrency and resource limits.

### Project 4: Producer-Consumer System

Build a producer that generates jobs and a consumer that processes them. Implement one version using threads and another using `asyncio.Queue`.

**Goal:** Understand queues, synchronization, and task coordination.

---

## 14. Recommended Learning Order

Follow this sequence:

1. **Timing:** `timeit`, `time.perf_counter()`.
2. **Profiling:** `cProfile`, `pstats`.
3. **Concurrency fundamentals:** Concurrency vs. parallelism.
4. **Threading:** Threads, thread pools, locks, events.
5. **Multiprocessing:** Processes, pools, queues, shared values.
6. **Async fundamentals:** Coroutines, `async`, `await`.
7. **Async coordination:** `gather()`, tasks, timeouts, cancellation.
8. **Structured concurrency:** `TaskGroup`, queues, semaphores.
9. **Performance practice:** Benchmark and profile real programs.
10. **Competitive programming:** Apply algorithmic optimization before considering concurrency.

## ✅ Final Goal

By completing this module, you should understand how to measure performance, identify bottlenecks, and choose between sequential execution, threading, multiprocessing, and asynchronous programming.

**Remember:** First make the algorithm correct, then make it efficient, and finally measure whether your optimizations actually help.