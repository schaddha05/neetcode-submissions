class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, path):
            if i == len(nums):
                res.append(list(path))
                return
            
            # include nums[i]
            path.append(nums[i])
            dfs(i+1, path)

            # skip nums[i]
            
            while (i+1) < len(nums) and nums[i] == nums[i+1]:
                i += 1 

            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        return res