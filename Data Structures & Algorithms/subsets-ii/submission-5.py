class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, subset):
            nonlocal res
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()
            j = i + 1 
            while j < len(nums) and nums[i] == nums[j]:
                j += 1 
            dfs(j, subset)
        
        dfs(0, [])
        return res