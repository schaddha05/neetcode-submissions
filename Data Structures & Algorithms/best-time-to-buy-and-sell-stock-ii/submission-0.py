class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res = 0 
        l = 0 
        for r in range(len(nums)):
            if nums[r] < nums[l]:
                l = r
            else:
                res += nums[r] - nums[l] 
                l = r
        
        return res 