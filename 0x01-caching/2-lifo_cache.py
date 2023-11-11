#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """Inherites from Basecaching"""
    def __init__(self):
        """Initializes the class"""
        super().__init__()
        self.order = []
    def put(self, key, item):
        """Allocates a given key to an item"""
        if key and item: 
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                discard = self.order.pop(0)
                print(f"DISCARD: {discard}")
                del self.cache_data[discard]
            self.order.append(key)
            self.cache_data[key] = item
    def get(self, key):
        """Gets the value of a given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]