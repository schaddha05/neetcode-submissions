class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i, jumps, cache):
            if i >= len(nums) -1:
                return jumps  
            if nums[i] == 0:
                return float('inf') 
            
            if (i, jumps) in cache:
                return cache[(i, jumps)]

            res = float('inf')
            for j in range(nums[i], 0, -1):
                res = min(res, dfs(i + j, jumps + 1, cache))

            cache[(i, jumps)] = res
            return cache[(i, jumps)]
        
        return dfs(0, 0, {})