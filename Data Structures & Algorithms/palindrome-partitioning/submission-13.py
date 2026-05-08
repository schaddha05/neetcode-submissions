class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i,j, path):
            if j == len(s):
                res.append(path.copy())
                return  
            if i == len(s):
                return
            
            segment = s[j:i+1]
            if segment == segment[::-1]:
                path.append(segment)
                dfs(i+1, i+1, path)
                path.pop()
                           
            dfs(i+1, j, path)
        
        dfs(0,0,[])
        return res