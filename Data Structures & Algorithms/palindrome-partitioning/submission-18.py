class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, path):
            if i == len(s):
                res.append(path.copy())
                return 
            
            for j in range(i, len(s)):
                segment = s[i: j + 1]
                if segment == segment[::-1]:
                    path.append(segment) 
                    dfs(j + 1, path)
                    path.pop() 
        dfs(0, [])
        return res
