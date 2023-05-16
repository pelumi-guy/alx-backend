#!/usr/bin/env python3
"""
1. Simple pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    A function that takes two integer arguments page and page_size and
    returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    those particular pagination parameters.
    """
    offset = 0 + ((page - 1) * page_size)

    return (offset, offset + page_size)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """
            A method that finds and returns the appropiate page of a dataset
            """
            assert type(page) is int and page > 0
            assert type(page_size) is int and page_size > 0

            dataset = self.dataset()
            row_indexes = index_range(page, page_size)

            if row_indexes[0] > len(row_indexes):
                return []

            if row_indexes[1] > len(row_indexes):
                row_indexes = (row_indexes[0], len(row_indexes) - 1)

if __name__ == '__main__':
    from pprint import pprint

    myServer = Server()

    dataset = myServer.dataset()

    pprint(type(dataset))
