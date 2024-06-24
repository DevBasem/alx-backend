#!/usr/bin/env python3
"""
Hypermedia pagination using Server class
"""
from typing import List, Dict, Union, Tuple
import math
from functools import lru_cache

Server = __import__('1-simple_pagination').Server


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start index and end index
    for a given pagination parameters.
    """
    return (page - 1) * page_size, (page - 1) * page_size + page_size


class Server(Server):
    """
    Server class extended to support hypermedia pagination.
    """

    def get_hyper(
        self,
        page: int = 1,
        page_size: int = 10
    ) -> Dict[str, Union[int, List[List[str]]]]:
        """
        Returns a dictionary with hypermedia pagination information.

        Args:
            page (int): 1-indexed page number.
            page_size (int): Number of items per page.

        Returns:
            Dict[str, Union[int, List[List[str]]]]: Dictionary containing
            pagination metadata and dataset page.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
