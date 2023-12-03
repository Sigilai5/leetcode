class RandomizedSet:

    def __init__(self):
        self.unique = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.unique:
            self.unique.add(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.unique:
            self.unique.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        list_unique = list(self.unique)
        rand_index = random.randint(0,len(list_unique) - 1)
        
        return list_unique[rand_index] 
        

    # SC -> O(N)
    # TC -> O(N)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()