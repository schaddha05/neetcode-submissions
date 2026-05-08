class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 

        prevRow = [float('inf')] * (amount + 1) 
        prevRow[0] = 0

        for i in range(1, len(coins) + 1):
            curRow = [float('inf')] * (amount + 1) 
            curRow[0] = 0
            for j in range(1, amount + 1):
                skip = prevRow[j]
                include = float('inf')
                if j - coins[i-1] >= 0:
                    include = 1 + curRow[j - coins[i-1]]
                curRow[j] = min(skip, include)
            prevRow = curRow 
        
        return -1 if prevRow[-1] == float('inf') else prevRow[-1]


        '''
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]
        
        for i in range(len(coins) + 1):
            dp[i][0] = 0 # for amount of 0, min coins we need is 0
       

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                skip = dp[i-1][j] 
                include = float('inf') 
                if j - coins[i-1] >= 0:
                    include = 1 + dp[i][j - coins[i-1]]
                
                dp[i][j] = min(skip, include) 
        
        return dp[len(coins)][amount] if dp[len(coins)][amount] != float('inf') else -1
        '''

            
            
            