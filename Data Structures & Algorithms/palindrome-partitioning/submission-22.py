class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False 
                l+= 1
                r-=1
            
            return True
        

        def dfs(i, temp):
            if i == len(s):
                res.append(temp.copy())
                return 
            
            for j in range(i, len(s)):
                if isPali(i,j):
                    temp.append(s[i:j+1])
                    dfs(j+1, temp)
                    temp.pop()
        
        dfs(0, [])
        return res
