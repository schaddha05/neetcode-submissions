class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False 
        
        def dfs(i, curSum, cache):
            if i >= len(nums) or  curSum > total / 2:
                return False
            if curSum == total / 2:
                return True 

            if (i, curSum) in cache:
                return cache[(i, curSum)]

            # include current number
            include = dfs(i+1, curSum + nums[i], cache)
            # skip current number
            skip = dfs(i+1, curSum, cache)

            cache[(i, curSum)] = include or skip 

            return cache[(i, curSum)]

        return dfs(0, 0, {})