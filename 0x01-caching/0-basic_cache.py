#!/usr/bin/env python3
"""A class that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Inherites from Basecaching"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.cache_data = dict()

    def put(self, key, item):
        """Allocates a given key to an item"""
        if key or item is None:
            pass
        self.cache_data[key] = item
    def get(self, key):
        """Gets the value of a given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
        