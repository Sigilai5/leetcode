class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []        

    def push(self, val: int) -> None:
        if self.stack:
            new_min = min(val,self.min[-1])
            self.min.append(new_min)
            self.stack.append(val)
        else:
            self.stack.append(val)
            self.min.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)
            self.min.pop(-1)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

    # SC -> O(N)
    # TC -> O(1)

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()