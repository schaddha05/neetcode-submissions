class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack and val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            if not self.minStack:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]

        
