class MinStack:

    def __init__(self):
        self.min_num = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val,val))
        else:
            last_min = self.stack[-1][1]
            self.min_num = min(val,last_min)     
            self.stack.append((val,self.min_num))   

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
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