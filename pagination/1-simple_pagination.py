#!/usr/bin/env python3
"""This module contains the function index_range and the class Server
to paginate a database of popular baby names."""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Returns tuple containing start index and end index."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Takes two arguments page and page_size
        Returns items between start index and end index."""
        assert page > 0 and isinstance(page, int)
        assert page_size > 0 and isinstance(page_size, int)
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
