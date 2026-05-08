class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for num in unique:
            if num-1 not in unique:
                curr = num
                length = 0
                while curr in unique:
                    length+=1
                    curr+=1
                longest = max(length, longest)

        return longest

