class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        target = sum(nums) / 2 
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            newDP = dp.copy()
            for s in dp:
                newDP.add(nums[i] + s)

            dp = newDP

        return target in dp
