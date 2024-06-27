#!/usr/bin/python3
""" FIFOCache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements FIFO caching """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.queue = []  # to maintain order of keys (FIFO order)

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # FIFO eviction: remove the first item added
                if self.queue:
                    oldest_key = self.queue.pop(0)
                    del self.cache_data[oldest_key]
                    print("DISCARD:", oldest_key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None
