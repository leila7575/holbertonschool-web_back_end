#!/usr/bin/env python3
"""
This module contains the function to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int OR float v as arguments
    and returns a tuple where the first element is k
    and the second is quare of v
    """
    return (k, v ** 2)
