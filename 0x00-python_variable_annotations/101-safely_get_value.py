#!/usr/bin/env python3
"""
module that provides a function for safely getting
a value from a mapping
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Returns:
        Union[Any, T]: The value for the key in the mapping,
        or the default value if the key is not in the mapping
    """
    if key in dct:
        return dct[key]
    else:
        return default
