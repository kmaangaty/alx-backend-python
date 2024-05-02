#!/usr/bin/env python3
"""
Module that provides a function for summation of list values.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Parameters:
        input_list (List[float]): The list of float values to be summed.

    Returns:
        float: The sum of the values in the input list.
    """
    return sum(input_list)
