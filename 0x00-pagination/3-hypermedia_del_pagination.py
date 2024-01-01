#!/usr/bin/env python3

import csv
from typing import List, Dict, Optional

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None, page_size: int = 10) -> Dict:
        """Retrieve hypermedia information for a specific index.

        Args:
            index (int, optional): The start index of the return page. Defaults to None.
            page_size (int, optional): The size of each page. Defaults to 10.

        Returns:
            dict: Hypermedia information containing index, next_index, page_size, and data.
        """
        assert index is None or (isinstance(index, int) and 0 <= index < len(self.indexed_dataset())), "Index is out of range"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        if index is None:
            index = 0

        next_index = index + page_size
        dataset_page = [self.indexed_dataset()[i] for i in range(index, min(next_index, len(self.indexed_dataset())))]

        return {
            "index": index,
            "next_index": next_index if next_index < len(self.indexed_dataset()) else None,
            "page_size": len(dataset_page),
            "data": dataset_page
        }

server = Server()
server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")        
