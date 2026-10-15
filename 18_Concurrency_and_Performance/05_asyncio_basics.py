import asyncio

# Basic coroutine
async def greet(name):
    print(f"Hello, {name}")
    await asyncio.sleep(0.1)
    print(f"Goodbye, {name}")

# Run
asyncio.run(greet("Alice"))

# Multiple coroutines
async def task(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        task("A", 0.3),
        task("B", 0.1),
        task("C", 0.2),
    )

asyncio.run(main())

# Sequential vs concurrent
async def sequential():
    await task("1", 0.1)
    await task("2", 0.1)
    await task("3", 0.1)

async def concurrent():
    await asyncio.gather(
        task("1", 0.1),
        task("2", 0.1),
        task("3", 0.1),
    )

import time
start = time.perf_counter()
asyncio.run(sequential())
print(f"Sequential: {time.perf_counter() - start:.2f}s")

start = time.perf_counter()
asyncio.run(concurrent())
print(f"Concurrent: {time.perf_counter() - start:.2f}s")