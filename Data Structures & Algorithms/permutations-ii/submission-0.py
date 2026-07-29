class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = collections.defaultdict(int)

        for n in nums:
            count[n] += 1
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(list(path))
                return 
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    path.append(n)
                    dfs(path)
                    count[n] += 1
                    path.pop()
        
        dfs([])
        return res

       
