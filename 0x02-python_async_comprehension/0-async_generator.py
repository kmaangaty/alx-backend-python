#!/usr/bin/env python3
"""
Async generator coroutine that
yields random numbers asynchronously.

This coroutine loops 10 times,
each time asynchronously waiting for 1 second,
then yields a random number between 0 and 10.

Returns:
    Generator: Asynchronous
    generator object that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator coroutine.

    Yields:
        float: A random floating-point
         number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
