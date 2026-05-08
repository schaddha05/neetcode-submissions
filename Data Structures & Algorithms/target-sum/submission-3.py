class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # default dict maps targetSum to number of ways we can achieve it
        dp = [defaultdict(int) for i in range(len(nums) + 1)]
        dp[0][0] = 1 # the number of ways we can achieve sum of 0 from 0 elements is 1

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                # i + 1 means we have 1 extra element available now
                dp[i+1][cur_sum + nums[i]] += count
                dp[i+1][cur_sum - nums[i]] += count
        
        return dp[len(nums)][target]

