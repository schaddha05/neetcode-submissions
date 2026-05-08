class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        num = nums[0]
        without_num = self.subsets(nums[1:])
        with_num = []
        for s in without_num:
            with_num.append([num] + s) 
        
        return without_num + with_num