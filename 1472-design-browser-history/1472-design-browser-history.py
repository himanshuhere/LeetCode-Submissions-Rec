class BrowserHistory:
    #2 STACK - History will always have one current page as element becasue rwe return hist[-1], there should be something there always  bcs 'Return the current url after moving back in history at most steps.'
    #future one dsnt need
    
    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history.pop())
            steps -= 1
        return self.history[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.future:
            self.history.append(self.future.pop())
            steps -= 1
        return self.history[-1]