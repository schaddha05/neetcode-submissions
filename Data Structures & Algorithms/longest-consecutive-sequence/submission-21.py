class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums) 
        res = 0

        for num in nums:
            if num - 1 in numbers:
                continue 
            
            curr = 0
            while num in numbers:
                curr += 1
                num = num + 1

            res = max(res, curr) 
        
        return res
        