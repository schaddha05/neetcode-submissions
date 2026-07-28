class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, nums):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = dfs(i+1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(j, nums[i]) # add current number of permutations of rest of list
                    resPerms.append(p_copy)
            
            return resPerms
        
        return dfs(0, nums)