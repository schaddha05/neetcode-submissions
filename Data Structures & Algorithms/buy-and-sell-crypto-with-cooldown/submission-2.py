class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0 
            
            if canBuy: # can either buy or skip
                buy = - prices[i] + dfs(i+1, False)
                skip = dfs(i+1, True)
                return max(buy, skip)
            else:
                sell = prices[i] + dfs(i+2, True)
                skip = dfs(i+1, False) 
                return max(sell, skip)

        return dfs(0, True)