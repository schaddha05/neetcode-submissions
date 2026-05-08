class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
        unique.sort()

        left = 0
        maxLength = 1
        for right in range(1, len(unique)):
            if unique[right] != unique[right-1] + 1:
                left = right 
            else:
                maxLength = max(maxLength, right - left + 1)
        
        return maxLength
