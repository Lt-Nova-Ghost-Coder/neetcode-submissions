class MyHashSet:

    def __init__(self):
        self.hashArray = [-1] * ((10 ** 6) + 1)
        

    def add(self, key: int) -> None:
        self.key = key
        self.hashArray[self.key] = self.key
        

    def remove(self, key: int) -> None:
        self.key = key
        self.hashArray[self.key] = -1
        

    def contains(self, key: int) -> bool:
        self.key = key
        if self.hashArray[self.key] == self.key:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)