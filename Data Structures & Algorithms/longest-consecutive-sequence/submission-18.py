class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxResult = 0
        for num in nums:
            if num-1 not in unique:
                current = num
                result =0 
                while current in unique:
                    result+=1
                    current+=1
                maxResult = max(maxResult, result)
        return maxResult