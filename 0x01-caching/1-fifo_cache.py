#!/usr/bin/env python3
"""
Task 1: FIFO caching
"""


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class"""
    def __init__(self):
        """initialize class"""
        super().__init__()
        self.fetch = deque()

    def put(self, key, item):
        """
        assign an item value for the key
        to a dictionary.
        """
        if key is None or item is None:
            return
        capacity = BaseCaching.MAX_ITEMS
        self.cache_data[key] = item
        self.fetch.append(key)
        if key in self.cache_data:
            self.cache_data[key] = item
        if len(self.cache_data) >= capacity:
            key_to_pop = self.fetch.popleft()
            del self.cache_data[key_to_pop]
            print(f"DISCARD: {key_to_pop}")

    def get(self, key):
        """"""
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)
