class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = max(nums)
        minSum = min(nums)
        curMax = 0
        curMin = 0

        for num in nums:
            if curMax < 0:
                curMax = 0     
            if curMin > 0:
                curMin = 0 
            
            curMax += num
            curMin += num
            maxSum = max(curMax, maxSum)
            minSum = min(curMin, minSum)
        
        if sum(nums) == minSum:
            return maxSum
        else:
            return max(maxSum, sum(nums) - minSum)
            