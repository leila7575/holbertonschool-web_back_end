#!/usr/bin/env python3
"""This module contains the function index_range."""


def index_range(page, page_size):
    """Returns tuple containing start index and end index."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
