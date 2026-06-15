class RandomizedSet:

    def __init__(self):
        self.hashSet = set()
        import random
        

    def insert(self, val: int) -> bool:
        self.val = val
        if self.val not in self.hashSet:
            self.hashSet.add(self.val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        self.val = val
        if self.val in self.hashSet:
            self.hashSet.remove(self.val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        if not self.hashSet:
            return None
        else:
            return next(iter(self.hashSet))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()