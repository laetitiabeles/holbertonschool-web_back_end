#!/usr/bin/env python3
""" Returns 10 random numbers using an async comprehension
Return a list comprehension with await syntax
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Returns a list of 10 random float values
    This uses an async generator to return a list comprehension
    with awaited values.
    """
    return [delay async for delay in async_generator()]
