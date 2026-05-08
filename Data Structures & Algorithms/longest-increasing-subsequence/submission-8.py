class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, j, cache):
            if i == len(nums):
                return 0 
            if (i, j) in cache:
                return cache[(i,j)]

            skip = dfs(i+1, j, cache)

            take = 0
            if j == -1 or nums[i] > nums[j]:
                take = 1 + dfs(i+1, i, cache)
            
            cache[(i,j)] =  max(skip, take) 
            return cache[(i,j)] 
        
        return dfs(0, -1, {})
