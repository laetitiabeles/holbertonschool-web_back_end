#!/usr/bin/env python3

'''
Program that execute multiple coroutines concurrently
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Asynchronous coroutine that takes in
    two integer arguments and returns a list of floats
    '''
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
