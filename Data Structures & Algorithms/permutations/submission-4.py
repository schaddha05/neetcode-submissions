class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            item = nums[i]
            nums_without_item = [num for num in nums if num != item]
            permutations = self.permute(nums_without_item)
            for p in permutations:
                res.append([item] + p)
        
        return res
