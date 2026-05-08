class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min number of coins that would sum up to index value
        # ie for example 1, dp[1] = 1 since it only takes one coin to sum up to value of 1 since 1 is in coins list
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                  dp[i] = min(dp[i], 1 + dp[i-c]) # for example 1, min(1 + dp[11], 1 + dp[7], 1 + dp[2])

        return -1 if dp[amount] == float('inf') else dp[amount]

