class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recursive(i, cache): 
            if i >= len(nums):
                return 0 
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + recursive(i+2, cache), recursive(i+1, cache))
            return cache[i]
        
        return recursive(0, {})