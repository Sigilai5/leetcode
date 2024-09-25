import random 

class RandomizedSet:

    def __init__(self):
        self.val_index = {}
        self.vals = []        

    def insert(self, val: int) -> bool:
        if val in self.val_index: return False

        self.val_index[val] = len(self.vals)
        self.vals.append(val)
        return True        

    def remove(self, val: int) -> bool:
        if val not in self.val_index: return False

        # get last item
        last_item = self.vals[-1]
        # get index to replace
        idx = self.val_index.get(val)

        # delete from map
        self.val_index[last_item] = idx
        self.val_index.pop(val)

        # delete from list
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