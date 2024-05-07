#!/usr/bin/env python3
"""Module documentation"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache (BaseCaching):
    """BasicCache class"""

    def __init__(self):
        """init constructor"""
        super().__init__()

    def put(self, key, item):
        """put items in the dictionnary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get items from the dictionnary"""
        if key is None or not self.cache_data.get(key):
            return None
        return self.cache_data[key]
