class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def findSubsets(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            findSubsets(i + 1, subset + [nums[i]])
            findSubsets(i + 1, subset)
        
        findSubsets(0, [])
        return res