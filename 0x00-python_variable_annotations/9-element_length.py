#!/usr/bin/env python3
"""Let's duck type an iterable object"""

from typing import List, Iterable, Sequence, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Determines the length of an element"""
    return [(i, len(i)) for i in lst]
