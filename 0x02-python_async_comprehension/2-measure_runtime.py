#!/usr/bin/env python3
"""
Module provides a coroutine to measure
 the runtime of executing
the async_comprehension coroutine four times in parallel.
"""

import asyncio
import time
from importlib import import_module

# Importing async_comprehension coroutine from the previous file
async_comprehension = import_module('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of executing
    the async_comprehension coroutine
    four times in parallel.

    Returns:
        float: The total runtime
         in seconds.
    """
    # Record the start time
    start_time = time.time()

    # Execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    # Calculate the total runtime
    total_runtime = time.time() - start_time

    return total_runtime
