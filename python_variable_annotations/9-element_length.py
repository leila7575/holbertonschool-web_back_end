#!/usr/bin/env python3
"""
This module contains the function element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes lst an iterable of sequences as argument
    Returns a list of tuples, which contains a sequence and the length(int)
    """
    return [(i, len(i)) for i in lst]
