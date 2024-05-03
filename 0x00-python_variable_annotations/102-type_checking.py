#!/usr/bin/env python3
"""
Function for zooming in on a tuple.
"""

from typing import Tuple, List, Any, Optional


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple:
    """
    Zooms in on the elements of a tuple by repeating each element a certain number of times.

    Args:
        lst (Tuple[Any, ...]): The tuple containing elements to be zoomed in on.
        factor (int, optional): The factor by which to zoom in. Defaults to 2.

    Returns:
        Tuple: A tuple containing the zoomed-in elements.
    """
    zoomed_in: Tuple = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: Tuple[int, int, int, int, int, int] = zoom_array(array)

zoom_3x: Tuple[int, int, int, int, int, int, int, int, int] = zoom_array(array, 3)
