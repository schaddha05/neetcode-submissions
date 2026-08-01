class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # number -> index

        for i in range(len(nums)):
            x = target - nums[i] 
            if x in seen:
                return [min(seen[x], i), max(seen[x], i)]
            
            seen[nums[i]] = i
            