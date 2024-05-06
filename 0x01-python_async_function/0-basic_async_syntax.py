#!/usr/bin/env python3

"""
Async I/O Basics

This script demonstrates basic asynchronous I/O functionality using
Python's asyncio module.
It includes an asynchronous coroutine that waits for a random delay
and eventually returns it.

"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a
    random delay and eventually returns it.

    Args:
        max_delay (int, optional): The maximum delay
        in seconds (inclusive). Defaults to 10.

    Returns:
        float: The random delay that was waited for.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
