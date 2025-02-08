class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            last = self.stack[-1][1]
            get_min = min(val,last)
            self.stack.append((val,get_min))    
        else:
            self.stack.append((val,val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

    # SC -> O(N)
    # TC -> O(1)
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()