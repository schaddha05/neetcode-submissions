class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(cur_sum, i, path):
            nonlocal res
            if cur_sum == target:
                res.append(path.copy())
                return 
            
            if cur_sum > target or i >= len(nums):
                return 
            
            path.append(nums[i])
            dfs(cur_sum + nums[i], i + 1, path)

            path.pop()
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            
            dfs(cur_sum, j, path)
        
        dfs(0,0, [])
        return res
