from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ord_dict = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.ord_dict: return -1

        item = self.ord_dict.get(key)

        self.ord_dict.pop(key)

        self.ord_dict[key] = item

        return item
        

    def put(self, key: int, value: int) -> None:
        if key in self.ord_dict:
            self.ord_dict.pop(key)
        if len(self.ord_dict) >= self.capacity:
            self.ord_dict.popitem(last=False)

        self.ord_dict[key] = value

    # SC -> O(N)
    # TC -> O(1)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)