class OrderedStream:

    def __init__(self, n: int):
        self.stream = {}
        self.pointer = 1       

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value 
        output = []

        while self.pointer in self.stream:
            output.append(self.stream.get(self.pointer))
            self.pointer+=1
        
        return output

    # SC -> O(N)
    # TC -> O(N)


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)