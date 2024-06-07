#!/usr/bin/env python3
"""Safely get a value from an iterator"""


from typing import TypeVar, Any, Mapping, Union


T = TypeVar('T')


def safely_get_value(
                        dct: Mapping,
                        key: Any,
                        default: Union[T, None] = None) -> T | None:
    """Safely get a value from a list"""
    if key in dct:
        return dct[key]
    else:
        return default
