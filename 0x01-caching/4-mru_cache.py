#!/usr/bin/python3
""" MRUCache module """
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements MRU caching """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.queue = []  # to maintain order of keys (MRU order)

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # MRU eviction: remove the most recently used item (last item in queue)
                if self.queue:
                    mru_key = self.queue.pop()
                    del self.cache_data[mru_key]
                    print("DISCARD:", mru_key)

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
