#!/usr/bin/env python3

'''
This module measures the runtime of a function using concurrent coroutines.
'''

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''
    Asynchronous coroutine that takes in two
    integer arguments and returns a float
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
