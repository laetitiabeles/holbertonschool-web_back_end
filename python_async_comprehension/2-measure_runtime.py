#!/usr/bin/env python3
""" Measures the total runtime of execution of async_comprehension
in parallel using asyncio.gather
Will be executed 4 times in total
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the total runtime of async_comprehension executed
    concurrently 4 times. The runtime measured should not be too long.
    Returns:
        float: total runtime
    """
    task = [async_comprehension() for _ in range(4)]

    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*task)

    end_time = asyncio.get_event_loop().time()

    total_time = end_time - start_time

    return total_time
