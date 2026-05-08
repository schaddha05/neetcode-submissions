class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur_sum, i, path):
            nonlocal res
            if cur_sum == target:
                res.append(path.copy())
                return 
            
            if cur_sum > target or i >= len(nums): 
                return 
            
            path.append(nums[i])
            dfs(cur_sum + nums[i], i, path)

            path.pop()
            dfs(cur_sum, i + 1, path) 
        
        dfs(0,0, [])
        return res