#!/usr/bin/python3
""" LIFOCache that inherits from BaseCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class"""

    def __init__(self):
        """ Initializing the LIFOCache"""
        super().__init__()

    def put(self, key, item):
        """ Adding an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Getting an item by key"""
        if key is not None:
            return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
