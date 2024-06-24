#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with hypermedia pagination information based
        on index.

        Args:
            index (int): Starting index of the page. Defaults to None.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            Dict: Dictionary containing pagination metadata and dataset page.
        """
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        indexed_data = self.indexed_dataset()

        # If index is None or out of range, set index to 0
        if index is None or index < 0 or index >= len(indexed_data):
            index = 0

        # Adjust index to the nearest available index in indexed_data
        while index not in indexed_data:
            index += 1
            if index >= len(indexed_data):
                index = 0
                break

        data = []
        for i in range(index, index + page_size):
            if i in indexed_data:
                data.append(indexed_data[i])

        next_index = index + len(data)
        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }
