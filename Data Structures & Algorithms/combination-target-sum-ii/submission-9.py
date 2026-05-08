class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(cur_sum, i, path):
            nonlocal res
            if cur_sum == target:
                res.append(path.copy())
                return 
            
            if i >= len(nums) or cur_sum > target:
                return 
            
            path.append(nums[i])
            dfs(cur_sum + nums[i], i+1, path)
            
            j = i + 1 
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            path.pop()
            dfs(cur_sum, j, path)
        
        dfs(0, 0, [])
        return res