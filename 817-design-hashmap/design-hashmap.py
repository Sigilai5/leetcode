class MyHashMap:

    def __init__(self):
        self.items = []        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.items)):
            if key == self.items[i][0]:
                self.items[i][1] = value
                return 
        
        new_item = [key,value]
        self.items.append(new_item)        

    def get(self, key: int) -> int:
        for i in range(len(self.items)):
            if key == self.items[i][0]:
                return self.items[i][1] 
        
        return -1
        

    def remove(self, key: int) -> None:
        for i in range(len(self.items)):
            if key == self.items[i][0]:
                del self.items[i]
                return
        
       # SC -> O(N)
       # TC -> O(N)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)