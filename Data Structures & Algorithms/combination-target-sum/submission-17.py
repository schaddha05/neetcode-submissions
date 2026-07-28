class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, curSum):
            if curSum[0] == target:
                res.append(list(path))
                return  
            if curSum[0] > target or i >= len(nums):
                return 
            
            # add current number and stay at index i
            path.append(nums[i])
            curSum[0] += nums[i]
            dfs(i, path, curSum)

            # skip the current number and move onto index i + 1
            number = path.pop()
            curSum[0] -= number
            dfs(i+1, path, curSum)
        
        dfs(0, [], [0])
        return res

