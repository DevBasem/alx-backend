#!/usr/bin/env python3
"""
2-lifo_cache module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class inherits from BaseCaching and implements LIFO caching strategy
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        
        # Check if cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the last item added (LIFO)
            discarded_key, _ = next(iter(self.cache_data.items()))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
