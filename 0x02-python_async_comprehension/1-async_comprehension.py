#!/usr/bin/env python3
"""
Async Comprehension

This module defines a coroutine that collects 10 random numbers using an async comprehension
over async_generator.

Example:
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
"""

from typing import List


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension over async_generator.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [num async for num in async_generator()]

async_generator = __import__('0-async_generator').async_generator
