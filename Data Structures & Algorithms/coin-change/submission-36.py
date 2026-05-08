class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 

        def dfs(i, amount, cache):
            if amount == 0:
                return 0  
            if amount < 0 or i == len(coins):
                return float('inf')
            if (i, amount) in cache:
                return cache[(i, amount)]

            keep = 1 + dfs(i, amount - coins[i], cache)
            skip = dfs(i+1, amount, cache) 

            cache[(i, amount)] = min(keep, skip) 
            return cache[(i, amount)]
        
        res = dfs(0, amount, {})
        return res if res != float('inf') else -1
            
            
            