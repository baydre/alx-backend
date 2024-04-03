#!/usr/bin/env python3
"""
Task 0: Basic dictionary.
"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""
    def __init__(self):
        """initialize the class"""
        super().__init__()

    def put(self, key, item):
        """
        assign item to the dictionary self.cache_data
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
