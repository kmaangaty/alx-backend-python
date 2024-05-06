#!/usr/bin/env python3
"""
Concurrency with asyncio

This module demonstrates asynchronous concurrency
in Python using asyncio.
It includes a coroutine wait_n that spawns
wait_random n times with the specified max_delay.


"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random
    n times with the specified max_delay.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay in
        seconds for each coroutine.

    Returns:
        List[float]: The list of all the delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    delays = await asyncio.gather(*tasks)
    return sorted(delays)
