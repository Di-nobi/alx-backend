#!/usr/bin/env python3
"""A LRUV Caching file"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """A LRU Caching class"""
    def __init__(self):
        """Initializes the LRU Caching class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            if key in self.cache_data.keys():
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]