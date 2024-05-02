#!/usr/bin/env python3
"""
Module for summing list values containing mixed types.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum the elements in a list containing mixed types.

    Parameters:
        mxd_lst (List[Union[int, float]]): The list of mixed-type elements.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(mxd_lst)
