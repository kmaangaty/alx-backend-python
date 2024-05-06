#!/usr/bin/env python3
"""
Asynchronous Task Creation

This module defines a regular function
to create and return an asyncio task
to execute the wait_random coroutine
with a specified max_delay.
"""

import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio task
    to execute the wait_random coroutine.

    Args:
        max_delay (int): The maximum
        delay in seconds for wait_random.

    Returns:
        asyncio.Task: An asyncio task.
    """
    return asyncio.create_task(wait_random(max_delay))
