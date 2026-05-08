class StockSpanner:

    def __init__(self):
        self.stack = [] 

    def next(self, price: int) -> int:
        self.stack.append(price)
        top = price 
        span = 1
        r = len(self.stack) - 2
        while r > -1 and self.stack[r] <= top:
            span += 1
            r -= 1
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)