class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True 
        
        res = []
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