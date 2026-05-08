class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        

        def dfs(i, j, k, cache):
            if k == len(s3):
                return i == len(s1) and j == len(s2) 
            
            if (i, j, k) in cache:
                return cache[(i, j, k)]

            path1 = False
            path2 = False
            if i < len(s1) and s3[k] == s1[i]:
                path1 = dfs(i+1, j, k+1, cache)
            if j < len(s2) and s3[k] == s2[j]:
                path2 = dfs(i, j+1, k+1, cache)
            
            cache[(i, j, k)] = path1 or path2
            return cache[(i, j, k)]
             
        
        return dfs(0, 0, 0, {})
