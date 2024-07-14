from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Test Case 1: Cache hit and cache miss
print('***** Test Case 1 *****')
our_cache = LRUCache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # Output: 1
print(our_cache.get(2))  # Output: 2
print(our_cache.get(9))  # Output: -1

# Test Case 2: Cache capacity reached
print('***** Test Case 2 *****')
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # Output: -1

# Test Case 3: Empty cache
print('***** Test Case 3 *****')
our_cache = LRUCache(0)
our_cache.set(1, 1)
print(our_cache.get(1))  # Output: -1