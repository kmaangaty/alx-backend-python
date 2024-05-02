#!/usr/bin/env python3
"""
module for creating a function that multiplies
a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns:
        Callable[[float], float]: A function that multiplies a
        float by the multiplier
    """
    def multiply(n: float) -> float:
        """
        float: result of multiplying
        """
        return n * multiplier
    return multiply
