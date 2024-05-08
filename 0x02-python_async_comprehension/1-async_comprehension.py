#!/usr/bin/env python3
"""
Module provides a coroutine for generating a
 list of random numbers asynchronously.
"""

from typing import List
from importlib import import_module

# Importing async_generator coroutine from the previous task
async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generate a list of random floating-point
     numbers asynchronously.

    Uses an asynchronous comprehension over the
     async_generator coroutine
    to collect 10 random numbers.

    Returns:
        List[float]: A list of 10 random
         floating-point numbers.
    """
    # Using asynchronous comprehension to collect 10 random numbers
    return [num async for num in async_generator()]
