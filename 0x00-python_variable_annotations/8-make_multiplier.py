#!/usr/bin/env python3
"""
Module for creating a function that multiplies a float by a multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Parameters:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float as input and returns
         the result of multiplying it by the multiplier.
    """
    def multiply(n: float) -> float:
        """
        Multiply a float by the multiplier.

        Parameters:
            n (float): The float to be multiplied.

        Returns:
            float: The result of multiplying n by the multiplier.
        """
        return n * multiplier
    return multiply
