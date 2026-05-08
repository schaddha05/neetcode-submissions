class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        def dfs(i, j):
            if i == len(nums):
                return 0 
            
            longest = dfs(i+1, j)
            if j == -1 or nums[i] > nums[j]:
                longest = max(longest, 1 + dfs(i+1, i))
          
            return longest
        
        return dfs(0, -1)