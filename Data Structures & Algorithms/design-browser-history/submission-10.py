class BrowserHistory:

    def __init__(self, homepage: str):
        self.curPos = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        while self.curPos < len(self.history) - 1:
            self.history.pop()
        
        self.history.append(url)
        self.curPos = len(self.history) - 1
            
    def back(self, steps: int) -> str:
        while self.curPos > 0 and steps > 0:
            self.curPos -= 1
            steps -= 1
            
        return self.history[self.curPos]

    def forward(self, steps: int) -> str:
        while self.curPos < len(self.history) - 1 and steps > 0:
            self.curPos += 1
            steps -= 1
        
        return self.history[self.curPos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)