class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False 
        
        def dfs(i, curSum):
            if i >= len(nums):
                return False
            if curSum == total / 2:
                return True
            if curSum > total / 2:
                return False 

            # include current number
            include = dfs(i+1, curSum + nums[i])
            skip = dfs(i+1, curSum)

            return include or skip

        return dfs(0, 0)