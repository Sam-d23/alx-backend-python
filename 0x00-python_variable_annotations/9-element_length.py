#!/usr/bin/env python3
from typing import Iterable, List, Sequence, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple
    contains an element from the input 
    list along with its length.
    """
    return [(i, len(i)) for i in lst]
