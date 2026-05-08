class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLength = 0

        for num in unique:
            if num-1 not in unique:
                currentLength = 1
                while num+currentLength in unique:
                    currentLength+=1
                maxLength = max(maxLength, currentLength)
        return maxLength
            
            
