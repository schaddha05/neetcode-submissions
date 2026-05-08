class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def dfs(i, canBuy, p):
            if i >= len(prices):
                return p 
            
            if canBuy:
                return max(dfs(i+1, False, p - prices[i]), dfs(i+1, True, p))
            else:
                return max(dfs(i+2, True, p + prices[i]), dfs(i+1, False, p)) 


        return dfs(0, True, 0)