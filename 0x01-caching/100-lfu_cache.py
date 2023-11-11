#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class of the LFU Caching system"""
    def __init__(self):
        super().__init__()
        self.__order = dict()
    
    def put(self, key, item):
        """Adds Item to the cache system"""
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data.keys():
                discard = self.l_key()
                del self.cache_data[discard]
                del self.__order[discard]
                print(f"DISCARD: {discard}")
            if key  in self.cache_data:
                self.__order[key] += 1
            else:
                self.__order[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """Gets the key of the item"""
        if key and key in self.cache_data:
            if key not in self.__order:
                self.__order[key] = 0
            self.__order[key] += 1
            return self.cache_data[key]
        return None
    
    def l_key(self):
        """Gets the least used key"""
        get_keys = list(self.__order.keys())
        counter = 0
        for count in range(1, len(get_keys)):
            if self.__order[get_keys[count]] < self.__order[get_keys[counter]]:
                counter = count
        return get_keys[counter]
