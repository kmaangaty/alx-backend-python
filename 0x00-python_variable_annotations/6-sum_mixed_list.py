#!/usr/bin/env python3
"""
Module for summing list values.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returns:
        float: The sum of the elements in mxd_lst.
    """
    return sum(mxd_lst)
