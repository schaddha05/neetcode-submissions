class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(i, canBuy, cache):
            if i >= len(prices):
                return 0 
            
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            if canBuy: # can either buy or skip
                buy = - prices[i] + dfs(i+1, False, cache)
                skip = dfs(i+1, True, cache)
                cache[(i, canBuy)] = max(buy, skip)
                return cache[(i, canBuy)]
            else:
                sell = prices[i] + dfs(i+2, True, cache)
                skip = dfs(i+1, False, cache) 
                cache[(i, canBuy)] = max(sell, skip)
                return cache[(i, canBuy)]

        return dfs(0, True, {})