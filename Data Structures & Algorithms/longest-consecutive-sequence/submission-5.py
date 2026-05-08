class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        unique = []
        for num in nums:
            if num not in unique:
                unique.append(num)
        
        maxLength = 1 
        for i in range(len(unique)):
            target = unique[i] + 1
            currentLength = 1
            while target in unique:
                currentLength+=1
                maxLength = max(currentLength, maxLength)
                target+=1
        return maxLength
        
            
            
            
