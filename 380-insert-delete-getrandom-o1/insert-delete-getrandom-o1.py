class RandomizedSet:

    def __init__(self):
        self.unique = {}
        self.unique_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.unique:
            return False
        else:
            self.unique[val] = len(self.unique_list)
            self.unique_list.append(val)
            return True        

    def remove(self, val: int) -> bool:
        if val not in self.unique:
            return False
        else:
            last_element = self.unique_list[-1]
            index = self.unique.get(val)

            # remove from dictionary
            self.unique[last_element] = index
            self.unique.pop(val)
            # remove from list
            self.unique_list[index] = last_element
            self.unique_list.pop(-1)

            return True       
        

    def getRandom(self) -> int:
        return random.choice(self.unique_list)
        

        # SC -> O(N)
        # TC -> O(1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()