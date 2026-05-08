class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        dp = [defaultdict(int) for i in range(len(nums) + 1)]
        # dp[number of items available][curSum] = number of ways we can creat curSum with current # of items available 
        dp[0][0] = 1 

        for i in range(len(nums)):
            for curSum, count in dp[i].items():
                dp[i + 1][curSum + nums[i]] += count
                dp[i + 1][curSum - nums[i]] += count
        
        return dp[len(nums)][target]
