#!/usr/bin/env python3
"""
Module for finding the length of each element in a list of sequences.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Find the length of each element in a list of sequences.

    Parameters:
        lst (Iterable[Sequence]): The list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
         contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
