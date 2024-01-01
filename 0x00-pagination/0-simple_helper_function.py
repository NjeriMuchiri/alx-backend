#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple:
    """
    This method returns a tuple of start index and end index
    for a given page and page size.
    Page numbers are 1-indexed.

    Args:
        page (int): The page number.
        page_size (int): The size of each page.

    Returns:
        tuple: A tuple containing start index and end index for
        the specified page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
