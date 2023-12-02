class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = 0
       
    def push(self, val: int) -> None:
        if len(self.stack) <= 0:
            self.stack.append((val,val)) 
        else:
            last_min = self.stack[-1][1]
            self.min_val = min(val,last_min)
            self.stack.append((val,self.min_val))       

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