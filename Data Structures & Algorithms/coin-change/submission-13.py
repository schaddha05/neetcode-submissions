class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(i, amt, cache):
            if amt == 0:
                return 0 # found a valid path, 0 more coins needed
            if amt < 0:
                return float('inf') # went too far, current path cannot make up amount
            if i >= len(coins):
                return float('inf') # exhausted all coins without making up the amount
            if (i, amt) in cache:
                return cache[(i, amt)]
            
            use = 1 + dfs(i, amt - coins[i], cache) 
            skip = dfs(i+1, amt, cache)
            cache[(i, amt)] = min(use, skip)
            return cache[(i, amt)]   

        res = dfs(0, amount, {}) 
        return -1 if res == float('inf') else res