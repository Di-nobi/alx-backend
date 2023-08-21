#!/usr/bin/env python3
"""Implementation of a function method that takes same argument as the get_page function and returns a dictionary"""
import math
import csv
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''a function named index_range that takes two integer arguments page and page_size'''
    start_page = (page - 1) * page_size
    stop_page = page * page_size
    return (start_page, stop_page)
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
        """Checks if page and page size is an integer and then return the dataset of the arguments"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        set_data = self.dataset()
        new_data = len(set_data)
        index, last = index_range(page, page_size)
        if index > new_data:
            return []
        return self.dataset()[index:last]
    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Hyper method that returns a dictionary containing the key-value pairs"""
        get_data = self.dataset()
        len_data = len(get_data)
        data = self.get_page(page, page_size)
        total_pages = (len_data + page_size - 1) // page_size
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
