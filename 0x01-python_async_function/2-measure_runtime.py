#!/usr/bin/env python3
"""
Measure Runtime

This module includes a function to measure the
runtime of the wait_n coroutine.
"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for
    wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay
        in seconds for each coroutine.

    Returns:
        float: The average execution time per coroutine.
    """
    waits = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(waits)
