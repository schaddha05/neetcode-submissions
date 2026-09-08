class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i] - 1 in unique:
                continue 
            cur = 1 
            x = nums[i]
            while x + 1 in unique:
                cur += 1
                x += 1
            res = max(res, cur)
        
        return res
        



