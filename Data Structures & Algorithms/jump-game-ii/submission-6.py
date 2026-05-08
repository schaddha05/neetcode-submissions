class Solution:
    def jump(self, nums: List[int]) -> int:
        def dfs(i, jumps):
            if i >= len(nums) -1:
                return jumps  
            if nums[i] == 0:
                return float('inf') 

            res = float('inf')
            for j in range(nums[i], 0, -1):
                res = min(res, dfs(i + j, jumps + 1))

            return res
        return dfs(0, 0)