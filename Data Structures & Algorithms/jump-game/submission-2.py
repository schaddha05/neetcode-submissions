class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(i, cache):
            if i == len(nums) - 1:
                return True 
            if i >= len(nums) or nums[i] == 0:
                return False 
            if i in cache:
                return cache[i]

            for j in range(nums[i], 0, -1):
                if dfs(i + j, cache):
                    cache[i] = True 
                    return True 
                
            cache[i] = False
            return cache[i] 
        
        return dfs(0, {})
            
            