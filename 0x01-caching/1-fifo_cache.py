#!/usr/bin/env python3
"""
1. FIFO caching
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A class that inherits from BaseCaching and is a caching system
    without limit
    """

    def __init__(self):
        super().__init__()
        self.cache_keys = deque()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            cache_data = self.cache_data
            cache_keys = self.cache_keys

            cache_data[key] = item
            if key not in cache_keys:
                cache_keys.append(key)

            if len(cache_keys) > self.MAX_ITEMS:
                oldest = cache_keys[0]
                print(f"DISCARD: {oldest}")
                cache_data.pop(oldest)
                cache_keys.popleft()

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)

        return None
