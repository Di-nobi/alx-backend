#!/usr/bin/env python3

from typing import Tuple
def index_range(page: int, page_size: int) -> Tuple[int, int]:
    stop_page = page * page_size
    start_page = (page - 1) * page_size
    return (start_page, stop_page)