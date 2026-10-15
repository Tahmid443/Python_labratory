import asyncio

async def worker(name, delay):
    print(f"{name}: start")
    await asyncio.sleep(delay)
    print(f"{name}: done")
    return f"{name}-result"

async def main():
    # create_task schedules coroutine
    task1 = asyncio.create_task(worker("A", 0.5))
    task2 = asyncio.create_task(worker("B", 0.3))

    # Do other work
    print("Doing other work...")
    await asyncio.sleep(0.1)

    # Wait for tasks
    r1 = await task1
    r2 = await task2
    print(r1, r2)

asyncio.run(main())

# TaskGroup (3.11+)
async def task_group_demo():
    try:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(worker("X", 0.2))
            t2 = tg.create_task(worker("Y", 0.1))
    except* Exception as eg:
        print(f"Errors: {eg.exceptions}")
    print("All done")

asyncio.run(task_group_demo())

# Queue
async def producer(q):
    for i in range(5):
        await q.put(i)
        await asyncio.sleep(0.1)
    await q.put(None)

async def consumer(q):
    while True:
        item = await q.get()
        if item is None:
            break
        print(f"Consumed: {item}")

async def queue_demo():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(queue_demo())

# Semaphore (limit concurrency)
async def limited(sem, name):
    async with sem:
        print(f"{name}: acquired")
        await asyncio.sleep(0.3)
        print(f"{name}: releasing")

async def sem_demo():
    sem = asyncio.Semaphore(2)
    await asyncio.gather(*[limited(sem, f"task{i}") for i in range(5)])

asyncio.run(sem_demo())