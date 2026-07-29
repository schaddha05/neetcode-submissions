class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        def dfs(i, path, nums):
            nonlocal length 
            if i == length:
                res.append(list(path))
                return 
            
            for j in range(len(nums)):
                cur = nums[j]
                path.append(cur)
                dfs(i+1, path, nums[:j] + nums[j+1:])
                path.pop()
                
        dfs(0, [], nums)
        return res
