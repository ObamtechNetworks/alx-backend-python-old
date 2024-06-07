#!/usr/bin/env python3
"""
Function that takes a lists of mixed types and returns their sum
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sum the list elements and returns the value as float

    Args:
        mxd_list (List[int, float]): mixed types in a list

    Returns:
        float: sum value
    """
    return sum(mxd_list)
