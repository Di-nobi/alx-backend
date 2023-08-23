#!/usr/bin/env python3
"""MRU Caching"""
from base_caching import BaseCaching
class MRUCache(BaseCaching):
    """Inherites from Basecaching"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.order = []
    def put(self, key, item):
        """Allocates a given key to an item"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                discard = self.order.pop(-1)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            if key in self.cache_data.keys():
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
    def get(self, key):
        """Gets the value of a given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]