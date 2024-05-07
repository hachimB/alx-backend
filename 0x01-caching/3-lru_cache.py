#!/usr/bin/env python3
"""Module documentation"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """init constructor"""
        super().__init__()

    def put(self, key, item):
        """puts keys and values in self.cache_data dictionnary"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            left_key = next(iter(self.cache_data.keys()))
            self.cache_data.pop(left_key)
            print("DISCARD: {}".format(left_key))
        self.cache_data[key] = item

    def get(self, key):
        """gets the value of a key in self.cache_data dictionnary"""
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data[key]
