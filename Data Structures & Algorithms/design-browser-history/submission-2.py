class BrowserHistory:

    # def __init__(self, homepage: str):
    #     self.back_history = [homepage]
    #     self.front_history = []

    # def visit(self, url: str) -> None:
    #     self.back_history.append(url)
    #     self.front_history = []

    # def back(self, steps: int) -> str:
    #     while steps and len(self.back_history) > 1:
    #         self.front_history.append(self.back_history.pop())
    #         steps -= 1
    #     return self.back_history[-1]

    # def forward(self, steps: int) -> str:
    #     while steps and self.front_history:
    #         self.back_history.append(self.front_history.pop())
    #         steps -= 1
    #     return self.back_history[-1]

    # def __init__(self, homepage:str):
    #     self.history = [homepage]
    #     self.cur = 0

    # def visit(self, url: str) -> None:
    #     self.cur += 1
    #     self.history = self.history[:self.cur]
    #     self.history.append(url)

    # def back(self, steps: int) -> str:
    #     self.cur = max(0, self.cur - steps)
    #     return self.history[self.cur]

    # def forward(self, steps: int) -> str:
    #     self.cur = min(len(self.history) - 1, self.cur + steps)
    #     return self.history[self.cur]

    def __init__(self, homepage:str):
        self.history = [homepage]
        self.cur  = 0
        self.n = 1

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
            self.n += 1
        else:
            self.history[self.cur] = url
            self.n = self.cur + 1

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
    
    def forward(self, steps: int) -> str:
        self.cur = min(self.n - 1, self.cur + steps)
        return self.history[self.cur]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)