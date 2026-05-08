class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        def dfs(i, amt, cache):
            if amt == 0:
                return 1 
            if i == len(coins) or amt < 0:
                return 0 
            if (i, amt) in cache:
                return cache[(i, amt)]

            skip = dfs(i+1, amt, cache)
            include = dfs(i, amt - coins[i], cache)

            cache[(i, amt)] = skip + include 
            return cache[(i, amt)]
        
        return dfs(0, amount, {})
