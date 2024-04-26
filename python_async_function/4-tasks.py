#!/usr/bin/env python3
""" Concurrent Coroutines """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of all the delays (float values) in ascending order """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
