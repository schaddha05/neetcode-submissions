class StockSpanner:

    def __init__(self):
        self.prices = [] # stores [price, span]


    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append([price, 1])
            return 1 
        
        res = 1 
        i = len(self.prices) - 1
        while i > -1 and self.prices[i][0] <= price:
            res += self.prices[i][1]
            i -= self.prices[i][1]
        
        self.prices.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)