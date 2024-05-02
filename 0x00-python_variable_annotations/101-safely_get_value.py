#!/usr/bin/env python3
"""
Module that provides a function for safely getting a value from a mapping.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely get a value from a mapping.

    Parameters:
        dct (Mapping): The mapping.
        key (Any): The key to look up in the mapping.
        default (Def, optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value for the key in the mapping,
        or the default value if the key is not in the mapping.
    """
    if key in dct:
        return dct[key]
    else:
        return default
