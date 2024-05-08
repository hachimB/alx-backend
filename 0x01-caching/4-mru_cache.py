#!/usr/bin/env python3
"""Module documentation"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """init constructor"""
        super().__init__()

    def put(self, key, item):
        """puts keys and values in self.cache_data dictionary"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            left_key = next(iter(self.cache_data.keys()))
            self.cache_data.pop(left_key)
            print("DISCARD: {}".format(left_key))
        self.cache_data[key] = item

    def get(self, key):
        """gets the value of a key in self.cache_data dictionary"""
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
