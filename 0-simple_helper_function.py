#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page, page_size):
    """
    Returns a tuple of start index and end index
    for a given pagination parameters.

    Args:
        page (int): 1-indexed page number.
        page_size (int): Number of items per page.

    Returns:
        tuple[int, int]: A tuple of integers representing
        start index (inclusive) and end index (exclusive)
        of the items for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
