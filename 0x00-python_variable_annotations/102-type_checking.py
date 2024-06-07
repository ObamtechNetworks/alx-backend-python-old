#!/usr/bin/env python3
"""Type checking using mypy Python package"""

from typing import List, Tuple, Callable, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
