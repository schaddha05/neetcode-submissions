class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        def dfs(amt, cache):
            if amt == 0:
                return 0
            if amt in cache:
                return cache[amt] # return the minimum number of coins needed to fulfill amt

            res = float('inf')
            for c in coins:
                if amt - c >= 0:
                    res = min(res, 1 + dfs(amt - c, cache))
            
            cache[amt] = res
            return cache[amt]
        
        res = dfs(amount, {})
        return res if res != float('inf') else -1
            

            