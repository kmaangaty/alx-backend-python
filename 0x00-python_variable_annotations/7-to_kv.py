#!/usr/bin/env python3
"""
Module for creating a tuple with a string and the
 square of an int or float as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string k and the square of v as a float.

    Parameters:
        k (str): The string key.
        v (Union[int, float]): The value, which can
        be either an int or a float.

    Returns:
        Tuple[str, float]: A tuple containing the string
         k and the square of v as a float.
    """
    return (k, float(v ** 2))
