#!/usr/bin/python3
""" LFUCache module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements LFU caching """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = {}  # to maintain frequency of each key
        self.freq_count = {}  # to maintain keys for each frequency

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequent used key(s)
                min_freq = min(self.freq_count.keys())
                lfu_keys = self.freq_count[min_freq]

                if len(lfu_keys) > 1:
                    # If there are multiple keys with the same frequency, use LRU to evict
                    lru_key = None
                    lru_time = float('inf')
                    for k in lfu_keys:
                        if k in self.cache_data and self.cache_data[k][1] < lru_time:
                            lru_key = k
                            lru_time = self.cache_data[k][1]
                    if lru_key:
                        del self.cache_data[lru_key]
                        self.frequency.pop(lru_key, None)
                        self.freq_count[min_freq].remove(lru_key)
                        print("DISCARD:", lru_key)
                else:
                    lfu_key = lfu_keys[0]
                    del self.cache_data[lfu_key]
                    self.frequency.pop(lfu_key, None)
                    self.freq_count[min_freq].remove(lfu_key)
                    print("DISCARD:", lfu_key)

            self.cache_data[key] = (item, 0)  # (item, access frequency)
            self.frequency[key] = 0
            self.freq_count[0] = self.freq_count.get(0, []) + [key]

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            if key in self.cache_data:
                item, freq = self.cache_data[key]
                # Update frequency
                self.frequency[key] += 1
                new_freq = self.frequency[key]
                self.freq_count[freq].remove(key)
                if not self.freq_count[freq]:
                    del self.freq_count[freq]
                self.freq_count[new_freq] = self.freq_count.get(new_freq, []) + [key]
                self.cache_data[key] = (item, new_freq)
                return item
        return None
