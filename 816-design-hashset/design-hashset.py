class MyHashSet:

    def __init__(self):
        self.unique = []
        

    def add(self, key: int) -> None:
        if key in self.unique:
            self.unique.remove(key)
        self.unique.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.unique:
            self.unique.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.unique:
            return True
        else:
            return False

    # SC -> O(N)
    # TC -> O(N)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)