class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        def dfs(i, curSum, cache):
            if i == len(nums) and curSum == target:
                return 1 
            
            if i == len(nums) and curSum != target:
                return 0 
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            add = dfs(i+1, curSum + nums[i], cache)
            subtract = dfs(i+1, curSum - nums[i], cache)

            cache[(i, curSum)] = add + subtract
            return cache[(i, curSum)]
            
        return dfs(0, 0, {})
