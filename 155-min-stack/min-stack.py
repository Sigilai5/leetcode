class MinStack:

    def __init__(self):
        self.vals = []        

    def push(self, val: int) -> None:
        if not self.vals:
            self.vals.append((val,val))   
        else:
            min_val = min(val,self.vals[-1][1])
            self.vals.append((val,min_val))

    def pop(self) -> None:
        if self.vals:
            self.vals.pop(-1)
        

    def top(self) -> int:
        if self.vals:
            return self.vals[-1][0]        

    def getMin(self) -> int:
        if self.vals:
            return self.vals[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()