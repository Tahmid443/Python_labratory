import asyncio

# Async function returns coroutine
async def fetch_data(id, delay):
    print(f"Fetching {id}")
    await asyncio.sleep(delay)
    return {"id": id, "data": f"result-{id}"}

# Awaiting
async def main():
    result = await fetch_data(1, 0.5)
    print(result)

asyncio.run(main())

# Gather
async def gather_demo():
    results = await asyncio.gather(
        fetch_data(1, 0.5),
        fetch_data(2, 0.3),
        fetch_data(3, 0.4),
    )
    for r in results:
        print(r)

asyncio.run(gather_demo())

# Timeout
async def slow():
    await asyncio.sleep(2)

async def timeout_demo():
    try:
        await asyncio.wait_for(slow(), timeout=0.5)
    except asyncio.TimeoutError:
        print("Timed out!")

asyncio.run(timeout_demo())

# Cancel
async def cancellable():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Cancelled!")
        raise

async def cancel_demo():
    task = asyncio.create_task(cancellable())
    await asyncio.sleep(0.1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass

asyncio.run(cancel_demo())

# Return exceptions
async def may_fail(n):
    if n == 2:
        raise ValueError("Failed")
    return n

async def return_exceptions():
    results = await asyncio.gather(
        may_fail(1), may_fail(2), may_fail(3),
        return_exceptions=True,
    )
    print(results)

asyncio.run(return_exceptions())