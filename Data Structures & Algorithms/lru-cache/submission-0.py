class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        self.key = key
        if self.key not in self.cache:
            return -1
        self.cache.move_to_end(self.key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        if self.key in self.cache:
            self.cache.move_to_end(self.key)
        self.cache[key] = self.value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

        
