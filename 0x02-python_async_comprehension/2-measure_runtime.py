#!/usr/bin/env python3

'''Task 2's module.
'''


import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures the
    total execution time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    total_runtime = loop.run_until_complete(measure_runtime())
    loop.close()

    print(f"Total runtime: {total_runtime:.15f} seconds")
