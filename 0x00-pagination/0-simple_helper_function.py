#!/usr/bin/env python3
"""Pagination Task"""
from typing import Tuple
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''a function named index_range that takes two integer arguments page and page_size'''
    start_page = (page - 1) * page_size
    stop_page = page * page_size
    return (start_page, stop_page)