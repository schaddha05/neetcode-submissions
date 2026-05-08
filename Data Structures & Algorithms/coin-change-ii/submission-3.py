class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1 
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                skip = dp[i-1][j]
                include = 0
                if j - coins[i-1] >= 0:
                    include = dp[i][j - coins[i-1]]

                dp[i][j] = skip + include

        return dp[len(coins)][amount]
        '''
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
        '''