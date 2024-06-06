#!/usr/bin/env python3
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples where each tuple
    contains an element from the input 
    list along with its length.
    """
    return [(i, len(i)) for i in lst]
