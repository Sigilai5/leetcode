import random

class RandomizedSet:

    def __init__(self):
        self.bucket = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.bucket:
            return False
            
        self.bucket[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.bucket:
            return False

        index, last_ele = self.bucket[val], self.values[-1]
        self.values[index] = last_ele
        self.bucket[last_ele] = index
        
        del self.bucket[val]
        self.values.pop()
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.values)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()