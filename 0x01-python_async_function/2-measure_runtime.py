#!/usr/bin/env python3
"""
Measure Runtime

This module includes a function to measure the
runtime of the wait_n coroutine.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
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
    time_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_end = time.time()
    return (time_end - time_start)/n
