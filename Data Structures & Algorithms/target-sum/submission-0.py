class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, curSum):
            if i == len(nums) and curSum == target:
                return 1 
            if i == len(nums) and curSum != target:
                return 0 
            
            add = dfs(i+1, curSum + nums[i])
            subtract = dfs(i+1, curSum - nums[i])

            return add + subtract 
        
        return dfs(0, 0)