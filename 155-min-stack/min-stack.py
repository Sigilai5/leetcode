class MinStack:

    def __init__(self):
        self.min_vals = []
        self.vals = []
        

    def push(self, val: int) -> None:
        if len(self.vals) == 0:
            self.vals.append(val)
            self.min_vals.append(val)
        else:
            self.vals.append(val)
            min_val = min(self.min_vals[-1],val)
            self.min_vals.append(min_val)
            

    def pop(self) -> None:
        self.vals.pop(-1)
        self.min_vals.pop(-1)
        
    def top(self) -> int:
        return self.vals[-1]
        

    def getMin(self) -> int:
        return self.min_vals[-1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()