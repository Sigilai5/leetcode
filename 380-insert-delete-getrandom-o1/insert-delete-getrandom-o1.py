import random
class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_index = {}        

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
            # Delete from dictionary
            last_item = self.vals[-1]
            idx = self.val_index.get(val)

            self.val_index[last_item] = idx
            self.val_index.pop(val)
        
            # Delete from array
            self.vals[idx] = last_item
            self.vals.pop(-1)

            return True

    def getRandom(self) -> int:
        rand_idx = random.randint(0,len(self.vals) - 1)
        return self.vals[rand_idx]


        # SC -> O(N)
        # TC -> O(1)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()