class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 

        def findSubsets(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            j = i
            findSubsets(i + 1, subset + [nums[j]])
            findSubsets(i + 1, subset)
        
        findSubsets(0, [])
        return res