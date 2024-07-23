class RandomizedSet:

    def __init__(self):
        self.key_val = {}
        self.vals = []        

    def insert(self, val: int) -> bool:
        if val in self.key_val: return False

        self.key_val[val] = len(self.vals)
        self.vals.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.key_val: return False

        # get last item and index to be deleted
        last_item = self.vals[-1]
        idx = self.key_val.get(val)

        self.key_val[last_item] = idx
        del self.key_val[val]
        
        self.vals[idx] = last_item
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