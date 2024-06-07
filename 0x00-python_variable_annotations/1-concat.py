#!/usr/bin/env python3
"""A module that defines a type annoated function
"""


def concat(str1: str, str2: str) -> str:
    """concatenates two strings

    Args:
        str1 (str): parameter 1, must be a string
        str2 (str): parameter 2, must be a string

    Returns:
        str: returns the concatenated string
    """
    return str1 + str2
