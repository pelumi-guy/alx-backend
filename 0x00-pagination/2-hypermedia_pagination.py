#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Dict


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
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        if end > len(dataset):
            end = len(dataset)

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        A method that takes the same arguments (and defaults) as get_page
        and returns a dictionary containing the following key-value pairs:
            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page (equivalent to return from previous task)
            - next_page: number of the next page, None if no next page
            - prev_page: number of the previous page, None if no previous page
            - total_pages: the total number of pages in the dataset
                as an integer
        """
        data = self.get_page(page, page_size)
        data_size = len(data)
        complete_data_size = len(self.__dataset)
        total_pages = math.ceil(complete_data_size / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': data_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
