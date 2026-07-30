class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for n in count:
                if count[n] > 0:
                    path.append(n)
                    count[n] -= 1
                    dfs(path)
                    path.pop()
                    count[n] += 1
        
        dfs([])
        return res


            
