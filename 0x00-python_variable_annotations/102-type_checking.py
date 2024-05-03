#!/usr/bin/env python3
"""
Module for zooming in on a tuple.
"""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """
    Zooms in on the elements of a tuple by repeating each element a certain number of times.

    Args:
        lst (Tuple): The tuple containing elements to be zoomed in on.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        List: A list containing the zoomed-in elements.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
