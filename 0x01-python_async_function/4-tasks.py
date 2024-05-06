#!/usr/bin/env python3
"""
Asynchronous Task Creation

This module defines a regular function to create and return asyncio tasks
to execute the wait_random coroutine multiple times with specified parameters.
"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and eventually returns it.

    Args:
        max_delay (int, optional): The maximum delay in seconds (inclusive). Defaults to 10.

    Returns:
        float: The random delay that was waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Regular function that creates and returns asyncio tasks
    to execute the wait_random coroutine n times with the specified max_delay.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay in seconds for each coroutine.

    Returns:
        List[float]: The list of all the delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = asyncio.run(asyncio.gather(*tasks))
    return sorted(delays)
