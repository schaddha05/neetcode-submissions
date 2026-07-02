class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        length = 0

        for i in range(len(nums)):
            if nums[i] -1 in uniqueNums:
                continue
            streak = 0
            cur = nums[i]
            while cur in uniqueNums:
                streak += 1
                cur += 1

            length = max(streak, length)
        
        return length