class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        dp = set()
        dp.add(0)
        target = sum(nums) / 2
        for i in range(len(nums)-1, -1, -1):
            newDP = dp.copy()
            for s in dp:
                if s + nums[i] == target:
                    return True 
                newDP.add(s + nums[i]) 
            dp = newDP
            
        return target in dp
            