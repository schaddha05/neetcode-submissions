class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        longest = 1
        for num in nums:
            if num - 1 not in set_nums:
                current = num + 1 
                streak = 1
                while current in nums:
                    streak += 1
                    current += 1
                longest = max(longest, streak)
        
        return longest
