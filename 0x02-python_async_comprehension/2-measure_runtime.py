#!/usr/bin/env python3
"""
Measure Runtime

This module defines a coroutine that executes async_comprehension four times in parallel
using asyncio.gather and measures the total runtime.

Example:
    async def main():
        return await(measure_runtime())

    print(asyncio.run(main()))
"""

import asyncio
from typing import List
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = perf_counter()
    return end_time - start_time
