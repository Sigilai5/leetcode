class RandomizedSet:

    def __init__(self):
        self.unique = set()
        
    def insert(self, val: int) -> bool:
        if val in self.unique: return False

        self.unique.add(val)
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.unique: return False

        self.unique.remove(val)
        return True
        

    def getRandom(self) -> int:
        output = list(self.unique)
        randIdx = random.randint(0,len(output)-1) 

        return output[randIdx]

        # SC -> O(N)
        # TC -> O(N)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()