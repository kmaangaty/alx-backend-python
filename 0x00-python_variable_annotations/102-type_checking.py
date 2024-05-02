#!/usr/bin/env python3
"""
Function for zooming in on a tuple.
"""
from typing import List, Tuple, Optional


def zoom_array(lst: Tuple[int, ...], factor: Optional[int] = 2) -> List[int]:
    """
    Zoom in on a tuple.

    Parameters:
        lst (Tuple[int, ...]): The tuple to zoom in on.
        factor (Optional[int], optional): The zoom factor. Defaults to 2.

    Returns:
        List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
