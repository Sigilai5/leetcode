class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = []
        self.current = 0
        self.pages.append(homepage)
        
    def visit(self, url: str) -> None:
        while len(self.pages) - 1 != self.current:
            self.pages.pop(-1)
        self.pages.append(url)
        self.current+=1

    def back(self, steps: int) -> str:
        self.current = max(0,self.current - steps)
        return self.pages[self.current]


    def forward(self, steps: int) -> str:
        self.current = min(len(self.pages) - 1, self.current + steps)
        return self.pages[self.current]

    # SC -> O(N)
    # TC -> O(N)
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)