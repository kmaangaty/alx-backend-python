#!/usr/bin/env python3
"""
function for zooming in on a tuple
"""
from typing import List, Tuple, Optional


def zoom_array(lst: Tuple[int, ...], factor: Optional[int] = 2) -> List[int]:
    """
    returns a list
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
