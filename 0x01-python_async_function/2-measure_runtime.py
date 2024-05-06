#!/usr/bin/env python3
"""
Measure Runtime

This module includes a function to measure the
runtime of the wait_n coroutine.
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_random


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
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
