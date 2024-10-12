class MinStack:

    def __init__(self):
        self.vals = []
        self.mins = []        

    def push(self, val: int) -> None:
        if len(self.vals) == 0:
            self.vals.append(val)
            self.mins.append(val)
        else:
            self.vals.append(val)
            min_val = min(self.mins[-1],val)
            self.mins.append(min_val)

    def pop(self) -> None:
        if self.vals:
            self.vals.pop(-1)
            self.mins.pop(-1)

    def top(self) -> int:
        if self.vals:
            return self.vals[-1]

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()