class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = nums[i] -1  # correct location for current element
            if  nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i+=1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]


