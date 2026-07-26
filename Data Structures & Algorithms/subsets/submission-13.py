class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, path):
            if i == len(nums):
                res.append(list(path))
                return 
            
            # either add current number or skip
            path.append(nums[i]) 
            dfs(i+1, path)

            path.pop()
            dfs(i+1, path)



        dfs(0, [])
        return res
            

