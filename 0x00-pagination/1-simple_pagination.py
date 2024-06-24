#!/usr/bin/env python3
"""
Pagination module for accessing and paginating a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start index and end index
    for a given pagination parameters.

    Args:
        page (int): 1-indexed page number.
        page_size (int): Number of items per page.

    Returns:
        tuple: A tuple of integers representing
        start index (inclusive) and end index (exclusive)
        of the items for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to handle dataset pagination.

    Attributes:
        DATA_FILE (str): Path to the dataset file.
        __dataset (List[List[str]]): Cached dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Cached dataset accessor.

        Returns:
            List[List[str]]: The dataset read from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Retrieve a specific page of the dataset based on pagination parameters.

        Args:
            page (int): 1-indexed page number (default: 1).
            page_size (int): Number of items per page (default: 10).

        Returns:
            List[List[str]]: A list of rows from the dataset corresponding
            to the requested page.
            Returns an empty list if the page is out of range.
        """
        assert isinstance(page, int) and page > 0, \
            "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        dataset = self.dataset()
        total_rows = len(dataset)

        start_index, end_index = index_range(page, page_size)

        if start_index >= total_rows:
            return []

        return dataset[start_index:end_index]
