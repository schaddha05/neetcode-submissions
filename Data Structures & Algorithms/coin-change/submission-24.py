class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(amt, cache):
            if amt == 0:
                return 0 
            
            if amt in cache:
                return cache[amt]
            
            res = float('inf')
            for c in coins:
                if amt - c >= 0:
                    res = min(res, 1 + dfs(amt - c, cache))
            
            cache[amt] = res
            return res
        
        res = dfs(amount, {})
        return -1 if res == float('inf') else res
