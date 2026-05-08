class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums) * 2
        newArr = [0] * size

        for i in range(len(nums)):
            newArr[i] = nums[i] 
        
        j = 0
        for i in range(len(nums), len(newArr)):
            newArr[i] = nums[j] 
            j += 1
        
        return newArr