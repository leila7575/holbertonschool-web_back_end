#!/usr/bin/env python3
"""
This module contains the function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list mxd_lst of floatsand integers as argument 
    and returns their sum as a float.
    """
    return sum(mxd_lst)
