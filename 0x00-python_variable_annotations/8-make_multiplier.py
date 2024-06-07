#!/usr/bin/env python3
"""A module returns a function that multiplies a float"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier that
    takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): a float parameter

    Returns:
        Callable[[float], float]: a callback function
    """
    def inner_function(x: float) -> float:
        """multiplies a float and return a float"""
        return x * multiplier

    return inner_function
