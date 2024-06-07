#!/usr/bin/env python3
"""Safely get a value from an iterator"""

from typing import TypeVar, Any, Mapping

T = TypeVar('T')


def safely_get_value(
                        dct: Mapping,
                        key: Any,
                        default: T | None = None) -> T | None:
    if key in dct:
        return dct[key]
    else:
        return default
