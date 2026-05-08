class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1 
        current = 1 
        prefix = [1] * len(nums)
        while i < len(nums):
            current *= nums[i-1]
            prefix[i] = current
            i += 1
        
        j = len(nums) - 2 
        current = 1
        while j > -1: 
            current *= nums[j+1]
            prefix[j] *= current
            j -= 1
        
        return prefix 
       

