class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin, = 1,1 # reset 
                continue
            else:
                temp = curMax
                curMax = max(n, curMax * n, curMin * n)
                curMin = min(n, curMin * n, temp * n)
            maxP = max(maxP, curMax)
        
        return maxP
                