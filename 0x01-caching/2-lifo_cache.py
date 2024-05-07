#!/usr/bin/env python3
"""Module documentation"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """init constructor"""
        super().__init__()

    def put(self, key, item):
        """puts keys and values in self.cache_data dictionnary"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """gets the value of a key in self.cache_data dictionnary"""
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data[key]
