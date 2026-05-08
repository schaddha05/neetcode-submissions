class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(i, cache, lst):
            if i >= len(lst):
                return 0 
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(lst[i] + solve(i+2, cache, lst), solve(i+1, cache, lst))
            return cache[i] 
        
        return max(solve(0, {}, nums[1:]), solve(0, {}, nums[:-1]))
