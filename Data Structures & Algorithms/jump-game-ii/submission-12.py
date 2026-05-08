class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i, cache):
            if i in cache:
                return cache[i] 
            if i >= len(nums) -1:
                return 0  
            if nums[i] == 0:
                return float('inf') 

            res = float('inf')
            for j in range(nums[i], 0, -1):
                res = min(res, 1+ dfs(i + j, cache))

            cache[i] = res
            return cache[i]
        
        return dfs(0, {})