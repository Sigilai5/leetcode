class OrderedStream:

    def __init__(self, n: int):
        self.stream = ["?"] * n # ["?","?","?","?","?"]
        self.pointer = 0        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value # ["?","?","CCCCC","?","?"]
        output = []

        while self.pointer < len(self.stream) and self.stream[self.pointer] != "?":
            output.append(self.stream[self.pointer])
            self.pointer+=1

        return output 

    # SC -> O(N)
    # TC -> O(N)


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)