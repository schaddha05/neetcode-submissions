class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]

        for i in range(len(nums)):
            curP = nums[i]
            maxP = max(curP, maxP)
            for j in range(i+1, len(nums)):
                curP *= nums[j]
                maxP = max(curP, maxP)

            
        return maxP
                