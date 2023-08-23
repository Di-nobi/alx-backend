#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key and item: 
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                discard = list(self.cache_data.keys())[-1]
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]