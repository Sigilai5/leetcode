class RandomizedSet:

    def __init__(self):
        self.val_index = {}
        self.vals = []
        

    def insert(self, val: int) -> bool:
        if val in self.val_index:
            return False
        else:
            self.val_index[val] = len(self.vals)
            self.vals.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.val_index:
            return False
        else:
            # delete from dictionary
            last_val = self.vals[-1]
            idx = self.val_index.get(val)

            self.val_index[last_val] = idx
            self.val_index.pop(val)

            # delete from list
            self.vals[idx] = last_val
            self.vals.pop(-1)
            return True

    def getRandom(self) -> int:
        return self.vals[random.randint(0,len(self.vals) -1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()