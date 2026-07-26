class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if len(path) == k:
                res.append(list(path))
                return
            if i > n:
                return 
            
            # add current number
            path.append(i)
            dfs(i+1, path)

            # skip current number
            path.pop()
            dfs(i+1, path)
        
        dfs(1, [])
        return res