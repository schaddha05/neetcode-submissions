class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def dfs(i, path):
            if i == len(nums):
                res.append(list(path))
                return 
            
            # accept nums[i]
            path.append(nums[i])
            dfs(i+1, path)

            # skip nums[i]
            path.pop()
            dfs(i+1, path)
        
        dfs(0, [])
        return res