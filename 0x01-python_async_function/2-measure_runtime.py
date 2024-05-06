#!/usr/bin/env python3
"""Contains a function that measures time to run wait_n"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
# If time.perf_counter() doesn't work change it to time.time()


async def measure_time(n: int, max_delay: int) -> float:
    """Measures time to run wait_n"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s

    return elapsed/n
