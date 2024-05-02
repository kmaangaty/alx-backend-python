#!/usr/bin/env python3
"""
Module for correct duck-typed annotations.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of the sequence, or None if the sequence is empty.

    Parameters:
        lst (Sequence[Any]): The sequence.

    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
