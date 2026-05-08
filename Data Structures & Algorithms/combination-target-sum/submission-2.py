class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs(cur_sum, start, path):
            if cur_sum == target:
                res.append(path.copy()) 
            
            if cur_sum > target:
                return 
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(cur_sum + nums[i], i, path)
                path.pop() 

        
        dfs(0, 0, []) 
        return res
