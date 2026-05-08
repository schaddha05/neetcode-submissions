class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0 
        skip = 0 

        for x in nums:
            new_rob = skip + x
            new_skip = max(rob, skip)
            rob, skip = new_rob, new_skip
            
        
        return max(rob, skip)
             
        '''
        def recursive(i, cache): 
            if i >= len(nums):
                return 0 
            
            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + recursive(i+2, cache), recursive(i+1, cache))
            return cache[i]
        
        return recursive(0, {})
        '''