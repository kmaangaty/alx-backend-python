#!/usr/bin/env python3
"""
Finding the length of each element in a list of strings.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns:
        List[Tuple[str, int]]: A list of tuples where each
        tuple contains a string and the length of that string.
    """
    return [(i, len(i)) for i in lst]
