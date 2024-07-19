class MyHashMap:

    def __init__(self):
        self.key_val = []
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.key_val)):
            if key == self.key_val[i][0]:
                self.key_val[i][1] = value  # Update value if key exists
                return
        self.key_val.append([key, value])  # Add new key-value pair if key does not exist
            

    def get(self, key: int) -> int:
        for i in range(len(self.key_val)):
            if key == self.key_val[i][0]:
                return self.key_val[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.key_val)):
            if key == self.key_val[i][0]:
                del self.key_val[i]
                return
    
    # SC -> O(N)
    # TC -> O(N)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)
