#!/usr/bin/env python3

'''
This module contains an async coroutine that return a delay
'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    Asynchronous coroutine that takes an integer argument and returns a float
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
