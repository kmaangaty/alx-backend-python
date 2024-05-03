#!/usr/bin/env python3
"""Task 12: Type Checking
"""
from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """Creates multiple copies of items in a tuple and returns them as a list.

    Args:
        lst (Tuple): The tuple containing items to be copied.
        factor (int, optional): The number of copies to create for each item. Defaults to 2.

    Returns:
        List: A list containing multiple copies of items from the input tuple.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
