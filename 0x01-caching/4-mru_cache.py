#!/usr/bin/env python3
"""
4. MRU Caching
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
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

            if len(cache_keys) >= self.MAX_ITEMS and key not in cache_keys:
                mru = cache_keys[-1]
                print(f"DISCARD: {mru}")
                cache_data.pop(mru)
                cache_keys.pop()
                # print('keys:', cache_keys)

            cache_data[key] = item
            if key not in cache_keys:
                cache_keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            if key in self.cache_keys:
                self.__replace(key)
            return self.cache_data.get(key)

        return None

    def __replace(self, key):
        """
        Shuffles the keys list to obtain
        least recently used item in the cache
        """
        cache_keys = self.cache_keys

        cache_keys.remove(key)
        cache_keys.append(key)
