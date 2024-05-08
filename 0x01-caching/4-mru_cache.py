#!/usr/bin/env python3
"""Module documentation"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """init constructor"""
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """puts keys and values in self.cache_data dictionary"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.mru_key)
            print("DISCARD: {}".format(self.mru_key))
        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """gets the value of a key in self.cache_data dictionary"""
        if key is None or key not in self.cache_data:
            return None
        self.mru_key = key
        return self.cache_data[key]

