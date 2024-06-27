#!/usr/bin/python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements LRU caching """

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.queue = []  # to maintain order of keys (LRU order)

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    lru_key = self.queue.pop(0)
                    del self.cache_data[lru_key]
                    print("DISCARD:", lru_key)

            self.cache_data[key] = item
            # Update the queue: move key to end to mark it as recently used
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            if key in self.cache_data:
                # Move key to end to mark it as recently used
                self.queue.remove(key)
                self.queue.append(key)
                return self.cache_data[key]
        return None
