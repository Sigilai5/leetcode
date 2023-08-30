class MinStack:

    def __init__(self):
        # initialize empty stack
        self.stack = []
               

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop(-1)
        
        
    def top(self) -> int:
        return self.stack[-1][0]
       

    def getMin(self) -> int:
        return self.stack[-1][1]

        # SC -> O(N)
        # TC -> O(1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()