class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        i = 0
        prefixProduct = 1
        while i < len(nums)-1:
           prefixProduct*= nums[i]
           result[i+1] = prefixProduct
           i+=1
        
        i = len(nums)-1
        postfixProduct = 1
        while i > 0: 
            postfixProduct*= nums[i]
            result[i-1] *= postfixProduct
            i-=1
        
        return result
        

        