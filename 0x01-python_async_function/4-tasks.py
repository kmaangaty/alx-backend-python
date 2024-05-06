#!/usr/bin/env python3
"""
This module defines a function to spawn wait_random coroutines
multiple times with specified parameters.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Spawns wait_random coroutines n times with the specified max_delay.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int, optional): The maximum delay in
        seconds for each coroutine. Defaults to 10.

    Returns:
        List[float]: List of all the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_interval_list = []
    for future in asyncio.as_completed(tasks):
        result = await future
        wait_interval_list.append(result)
    return wait_interval_list
