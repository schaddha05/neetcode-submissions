class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = val if not self.minStack or val < self.minStack[-1] else self.minStack[-1]
        self.minStack.append(new_min)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
