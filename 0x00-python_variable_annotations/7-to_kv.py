#!/usr/bin/env python3
"""
module for creating a tuple with a string
and square of an int or float as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns:
        Tuple[str, float]: A tuple with the string k and the
        square of v as a float
    """
    return (k, float(v ** 2))
