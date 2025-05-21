class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.key_val: return -1

        get_val= self.key_val.pop(key)
        
        self.key_val[key] = get_val

        return get_val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_val:
            self.key_val.pop(key)

        if len(self.key_val) >= self.capacity:
            self.key_val.popitem(last=False)
        
        self.key_val[key] = value
        

        # SC -> O(N)
        # TC -> O(1)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)