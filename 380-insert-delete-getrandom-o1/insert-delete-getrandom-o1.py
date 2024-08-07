class RandomizedSet:
    
    def __init__(self):
        self.vals = []
        self.val_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_idx: return False

        self.val_idx[val] = len(self.vals) 
        self.vals.append(val)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val_idx: return False

        last_item = self.vals[-1]
        idx = self.val_idx.get(val)

        self.val_idx[last_item] = idx
        self.vals[idx] = last_item

        self.val_idx.pop(val)
        self.vals.pop(-1)   
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)

# SC -> O(N)
# TC -> O(1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()