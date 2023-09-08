
# USING A LIST AND A POINTER
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.pages = []
#         self.pages.append(homepage)
#         self.current = 0
        

#     def visit(self, url: str) -> None:
#         while(len(self.pages) -1 != self.current):
#             self.pages.pop(-1)
#         self.pages.append(url)
#         self.current+=1
        

#     def back(self, steps: int) -> str:
#         self.current = max(0,self.current - steps)
#         return self.pages[self.current]
        

#     def forward(self, steps: int) -> str:
#         self.current = min(self.current + steps, len(self.pages) - 1)
#         return self.pages[self.current]
        

    # SC -> O(N)
    # TC -> O(1)

# USING A LINKED LIST

class ListNode:
    def __init__(self,page):
        self.page = page
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy = ListNode(homepage)
        self.curr = self.dummy   
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node
        

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev != None:
                self.curr = self.curr.prev
        
        return self.curr.page
       
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next != None:
                self.curr = self.curr.next
        
        return self.curr.page
       

# TC -> O(N)
# SC -> O(N)

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)