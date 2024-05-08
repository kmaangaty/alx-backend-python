#!/usr/bin/env python3

"""
Async Generator

This module defines an asynchronous generator coroutine that generates random numbers
asynchronously.

The coroutine async_generator loops 10 times, each time asynchronously waiting for 1 second,
then yields a random number between 0 and 10.

Example:
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)
"""

import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """
    Generate random numbers asynchronously.

    This coroutine loops 10 times, each time asynchronously waiting for 1 second,
    then yields a random number between 0 and 10 using the random.uniform function.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.uniform(0, 10)
