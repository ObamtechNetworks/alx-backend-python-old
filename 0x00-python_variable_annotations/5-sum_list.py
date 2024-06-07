#!/usr/bin/env python3
"""
Dealing with complex types
"""

from typing import Iterator


def sum_list(input_list: Iterator[float]) -> Iterator[float]:
    """

    Args:
        input_list (float]): a list of float types

    Returns:
        Iterator [float]: returns a list of floats
    """
    return sum(input_list)
