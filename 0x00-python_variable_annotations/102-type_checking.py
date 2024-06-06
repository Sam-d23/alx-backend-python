#!/usr/bin/env python3
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    '''
    Creates a zoomed-in version of the given
    array by repeating each element
    according to the specified factor.
    '''
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
