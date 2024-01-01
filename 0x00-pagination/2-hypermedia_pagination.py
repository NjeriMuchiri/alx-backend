#!/usr/bin/env python3

import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start index and end index for a
    a given page and page size.
    Page numbers are 1-indexed.

    Args:
        page (int): The page number.
        page_size (int): The size of each page.

    Returns:
        tuple[int, int]: A tuple containing start index
        and end index for the specified page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
        """method that retrieves a specific page of the dataset.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The size of each page. Defaults to 10.

        Returns:
            List[List]: The requested page of the dataset.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retrieve hypermedia information for a specific page.

        Args:
            page (int, optional): The page number. Defaults to 1.
            page_size (int, optional): The size of each page. Defaults to 10.

        Returns:
            dict: Hypermedia information containing page_size, page number,
            dataset page, next_page, prev_page, and total_pages.
        """
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset_page = self.get_page(page, page_size)
        start_index, _ = index_range(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if start_index + page_size < len(self.dataset()) else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
